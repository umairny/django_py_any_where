// Comment the user's post
function comm(id) {
    const editor = document.querySelector('#comment-editor-' + id);
    const commentInput = document.querySelector('#comment-' + id);
    const replyBtn = document.querySelector('#reply' + id);
    const comBtn = document.querySelector('#combtn' + id);
    const replyContainer = document.querySelector('#reply-container-' + id);
    const replyText = document.querySelector('#reply-' + id);

    if (editor) editor.style.display = 'block';
    if (comBtn) comBtn.style.display = 'none';
    if (commentInput) commentInput.focus();

    // Remove old listeners to avoid duplicates
    if (replyBtn) {
        const newReplyBtn = replyBtn.cloneNode(true);
        replyBtn.parentNode.replaceChild(newReplyBtn, replyBtn);

        newReplyBtn.addEventListener('click', () => {
            const val = commentInput.value.trim();
            if (!val) return;

            fetch('/network/comment/' + id, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ post: val })
            }).then(res => {
                if (res.ok) {
                    if (editor) editor.style.display = 'none';
                    if (replyContainer) replyContainer.style.display = 'block';
                    if (replyText) replyText.innerHTML = val;
                }
            }).catch(err => console.error('Error commenting:', err));
        });
    }
}

function cancelComment(id) {
    const editor = document.querySelector('#comment-editor-' + id);
    if (editor) editor.style.display = 'none';
    const comBtn = document.querySelector('#combtn' + id);
    if (comBtn) comBtn.style.display = 'inline-flex';
}

// Like and unlike the post
function like(id) {
    const likebtn = document.querySelector(`#like${id}`);
    const total_like = document.querySelector(`#total_like${id}`);
    const liked = document.querySelector(`#liked${id}`);

    fetch('/network/like/' + id, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ liked: "Like", post_id: id })
    })
        .then((res) => res.json())
        .then((res) => {
            if (res.status == 201) {
                if (total_like) total_like.innerHTML = res.total_like;
                if (liked) liked.innerHTML = res.liked;
                if (res.liked === "Liked") {
                    if (likebtn) likebtn.classList.add('liked');
                } else {
                    if (likebtn) likebtn.classList.remove('liked');
                }
            }
        }).catch(err => console.error('Error liking:', err));
}

// Follow/Unfollow users
function follow(id) {
    const total_follow = document.querySelector(`#total_follower`);
    const followBtn = document.querySelector(`#follow${id}`);

    fetch('/network/profile/' + id + '/follow', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ follow: "follow", user_id: id })
    })
        .then((res) => res.json())
        .then((res) => {
            if (res.status == 201) {
                if (total_follow) total_follow.innerHTML = res.total_follower;
                if (followBtn) followBtn.innerHTML = res.follow;
            }
        }).catch(err => console.error('Error following:', err));
}

// Edit post
function edit(id) {
    const content = document.querySelector('#post-content-container-' + id);
    const editor = document.querySelector('#editor-' + id);
    const editInput = document.querySelector('#edit-text-' + id);
    const saveBtn = document.querySelector('#save' + id);
    const editBtn = document.querySelector('#edit-btn-' + id);

    if (content) content.style.display = 'none';
    if (editor) editor.style.display = 'block';
    if (editBtn) editBtn.style.display = 'none';
    if (editInput) editInput.focus();

    if (saveBtn) {
        const newSaveBtn = saveBtn.cloneNode(true);
        saveBtn.parentNode.replaceChild(newSaveBtn, saveBtn);

        newSaveBtn.addEventListener('click', () => {
            const val = editInput.value.trim();
            if (!val) return;

            fetch('/network/edit/' + id, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ post: val })
            }).then(res => {
                if (res.ok) {
                    if (content) content.style.display = 'block';
                    if (editor) editor.style.display = 'none';
                    if (editBtn) editBtn.style.display = 'inline-flex';
                    const postElem = document.querySelector('#post-' + id);
                    if (postElem) postElem.innerHTML = val;
                }
            }).catch(err => console.error('Error editing:', err));
        });
    }
}

function cancelEdit(id) {
    const content = document.querySelector('#post-content-container-' + id);
    if (content) content.style.display = 'block';
    const editor = document.querySelector('#editor-' + id);
    if (editor) editor.style.display = 'none';
    const editBtn = document.querySelector('#edit-btn-' + id);
    if (editBtn) editBtn.style.display = 'inline-flex';
}
