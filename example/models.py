from django.db import models


class Position(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)

    def __unicode__(self):
        return u'%s,%s' % (self.lat, self.lng)

    class Meta:
        pass