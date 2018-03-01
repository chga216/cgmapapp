from tethys_sdk.base import TethysAppBase, url_map_maker


class Mapapp(TethysAppBase):
    """
    Tethys app class for Map App.
    """

    name = 'Map App'
    index = 'cgmapapp:home'
    icon = 'cgmapapp/images/Bike Logo.jpg'
    package = 'cgmapapp'
    root_url = 'cgmapapp'
    color = '#2E4A62'
    description = 'Preliminary layout of the Bike Route Planner app'
    tags = '&quot;514&quot;, &quot;Bike Route Planner&quot;, &quot;Mapplication&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='about',
                url='cgmapapp/about',
                controller='cgmapapp.controllers.about'
            ),
            UrlMap(
                name='home',
                url='cgmapapp',
                controller='cgmapapp.controllers.home'
            ),
            UrlMap(
                name='dataservices',
                url='cgmapapp/dataservices',
                controller='cgmapapp.controllers.dataservices'
            ),
            UrlMap(
                name='mapview',
                url='cgmapapp/mapview',
                controller='cgmapapp.controllers.mapview'
            ),
            UrlMap(
                name='proposal',
                url='cgmapapp/proposal',
                controller='cgmapapp.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='cgmapapp/mockup',
                controller='cgmapapp.controllers.mockup'
            ),
        )

        return url_maps
