from django.contrib.gis.db import models

from operations.models import Trainer, Location, Participant


class Event(models.Model):

    """
    Training events
    """
    trainer = models.ForeignKey(Trainer,
                                related_name='events',
                                null=False)
    location = models.ForeignKey(Location,
                                 related_name='events',
                                 null=False)
    scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "Training event by %s on %s" % (
            self.trainer, self.scheduled_at)


class Attendee(models.Model):

    """
    Participants at specific training events
    """
    event = models.ForeignKey(Event,
                              related_name='attendees',
                              null=False)
    participant = models.OneToOneField(Participant,
                                       related_name='participant',
                                       null=False)
    survey_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return "Attendee %s for event %s" % (self.participant, self.event)