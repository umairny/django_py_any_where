from django.db import models

# Create your models here.
class Headings(models.Model):
    heading = models.CharField(max_length=50)
    subHeading = models.CharField(max_length=500)
    icon = models.CharField(max_length=150, default="")
    btnApp = models.CharField(max_length=50)
    btnCode = models.CharField(max_length=200)
    videoLink = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.heading}"
    
class Features(models.Model):
    head = models.ForeignKey(Headings, on_delete=models.CASCADE)
    feature = models.CharField(max_length=500)
    def __str__(self) -> str:
        return f"{self.feature}"
    
class SubFeatures(models.Model):
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    sub_feature = models.CharField(max_length=500)
    def __str__(self) -> str:
        return f"{self.sub_feature}"