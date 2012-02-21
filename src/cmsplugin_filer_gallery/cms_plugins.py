from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
import models


class FilerGalleryPlugin(CMSPluginBase):
    model = models.FilerGallery
    name = _("Gallery")
    render_template = "cmsplugin_filer_gallery/gallery.html"
    text_enabled = False
    admin_preview = False
    
    def get_folder_images(self, folder, user):
        qs_files = folder.files.filter(_file_type_plugin_name='Image')
        if user.is_staff:
            return qs_files
        else:
            return qs_files.filter(is_public=True)
    
    def get_children(self, folder):
        return folder.get_children()
    
    def render(self, context, instance, placeholder):
        images = self.get_folder_images(instance.folder, context['request'].user)
        
        context.update({
            'object': instance,
            'thumbnail_option': instance.thumbnail_option,
            'size': (instance.thumbnail_option.width, instance.thumbnail_option.height),
            'crop': instance.thumbnail_option.crop,
            'upscale': instance.thumbnail_option.upscale,
            'images': images,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)