from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from filer.fields.folder import FilerFolderField
from cmsplugin_filer_image.models import ThumbnailOption

class FilerGallery(CMSPlugin):
    """
    Plugin for a gallery of images.
    """
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    folder = FilerFolderField()
    thumbnail_option = models.ForeignKey(ThumbnailOption, verbose_name=_("thumbnail option"))
    
    def __unicode__(self):
        if self.title: 
            return self.title;
        elif self.folder.name:
            return self.folder.name;
        return "<empty>"
    
    search_fields = ('title',)
    