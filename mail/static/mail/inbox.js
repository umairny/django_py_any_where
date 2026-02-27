document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

});

function update_nav_active(mailbox) {
  // Update active state in navigation
  document.querySelectorAll('.mail-nav-btn').forEach(btn => btn.classList.remove('active'));
  if (mailbox === 'archive') mailbox = 'archived';
  const activeBtn = document.querySelector(`#${mailbox}`);
  if (activeBtn) activeBtn.classList.add('active');
}

function load_mailbox(mailbox) {
  update_nav_active(mailbox);

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name/header
  document.querySelector('#emails-view').innerHTML = `
    <div class="mb-4 fade-in">
      <h2 class="font-weight-bold mb-1">${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h2>
      <div class="border-bottom opacity-10 mt-2" style="border-width: 2px;"></div>
    </div>
    <div id="emails-list" class="fade-in"></div>
  `;

  load_emails(mailbox);
}

function compose_email() {
  update_nav_active('compose');

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').onsubmit = function (event) {
    event.preventDefault();

    let recipients = document.querySelector('#compose-recipients').value;
    let subject = document.querySelector('#compose-subject').value;
    let body = document.querySelector('#compose-body').value;

    fetch('/mail/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body,
      })
    })
      .then(response => response.json())
      .then(result => {
        console.log(result);
        load_mailbox('sent');
      });
  };
}

function load_emails(mailbox) {
  fetch(`/mail/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      const list = document.querySelector("#emails-list");
      if (emails.length === 0) {
        list.innerHTML = `
          <div class="text-center py-5 glass-panel">
            <i class="fas fa-inbox fa-3x text-muted mb-3 opacity-20"></i>
            <p class="text-muted">No emails in ${mailbox}</p>
          </div>
        `;
        return;
      }

      emails.forEach(email => {
        const element = document.createElement("div");
        element.className = `email-item glass-panel fade-in ${email.read ? 'read' : 'unread'}`;

        element.innerHTML = `
          <div class="sender">
            <i class="fas ${mailbox === 'sent' ? 'fa-paper-plane' : 'fa-user'} mr-2 opacity-50"></i>
            ${mailbox === 'sent' ? email.recipients.join(', ') : email.sender}
          </div>
          <div class="subject">${email.subject}</div>
          <div class="timestamp">${email.timestamp}</div>
        `;

        element.addEventListener("click", () => read_email(email.id, mailbox));
        list.appendChild(element);
      });
    })
    .catch(error => console.error('Error:', error));
}

function read_email(id, mailbox) {
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector("#email").style.display = "block";
  document.querySelector("#email").innerHTML = "";

  fetch(`/mail/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      render_single_email(email, mailbox);

      // Set to read
      if (!email.read) {
        fetch(`/mail/emails/${id}`, {
          method: "PUT",
          body: JSON.stringify({ read: true })
        });
      }
    })
    .catch(error => console.error(error));
}

function render_single_email(email, mailbox) {
  const container = document.querySelector("#email");

  const header = document.createElement("div");
  header.className = "email-view-header glass-panel p-4 mb-4";
  header.innerHTML = `
    <div class="d-flex justify-content-between align-items-center mb-4">
        <button class="btn-wiki-outline btn-sm px-3" onclick="load_mailbox('${mailbox}')">
            <i class="fas fa-arrow-left mr-2"></i> Back to ${mailbox}
        </button>
        <div class="actions">
            ${mailbox !== 'sent' ? `
                <button id="archive-btn" class="btn btn-outline-info rounded-pill px-4 btn-sm font-weight-bold">
                    <i class="fas ${email.archived ? 'fa-box-open' : 'fa-archive'} mr-2"></i>
                    ${email.archived ? 'Unarchive' : 'Archive'}
                </button>
                <button id="reply-btn" class="btn btn-primary rounded-pill px-4 btn-sm font-weight-bold ml-2">
                    <i class="fas fa-reply mr-2"></i> Reply
                </button>
            ` : ''}
        </div>
    </div>
    <div class="email-meta">
        <h2 class="mb-3">${email.subject}</h2>
        <div class="d-flex justify-content-between text-muted small">
            <div>
                <strong>From:</strong> ${email.sender} <br>
                <strong>To:</strong> ${email.recipients.join(', ')}
            </div>
            <div class="text-right">
                ${email.timestamp}
            </div>
        </div>
    </div>
    <div class="email-body">${email.body}</div>
  `;

  container.appendChild(header);

  if (mailbox !== 'sent') {
    document.querySelector('#archive-btn').onclick = () => {
      fetch(`/mail/emails/${email.id}`, {
        method: "PUT",
        body: JSON.stringify({ archived: !email.archived })
      }).then(() => load_mailbox('inbox'));
    };

    document.querySelector('#reply-btn').onclick = () => {
      reply_email(email);
    };
  }
}

function reply_email(email) {
  compose_email();

  document.querySelector('h3').textContent = "Reply to Message";
  document.querySelector('#compose-recipients').value = email.sender;
  document.querySelector('#compose-subject').value = (email.subject.startsWith('Re:') ? '' : 'Re: ') + email.subject;
  document.querySelector('#compose-body').value = `\n\n-------------------\nOn ${email.timestamp} ${email.sender} wrote:\n\n${email.body}`;
  document.querySelector('#compose-body').focus();
  document.querySelector('#compose-body').setSelectionRange(0, 0);
}
