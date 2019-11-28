from Jumpscale import j

class Package(j.baseclasses.threebot_package):
    """
    to start need to run 
    kosmos -p 
    JSX> cl = j.servers.threebot.local_start_zerobot_default() 
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/Incubaid/www_incubaid/")
    """
    def _init(self, **kwargs):
        self.branch = kwargs["package"].branch or "master"
        self.incubaid = "https://github.com/Incubaid/www_incubaid"

    def prepare(self):
        """
        called when the 3bot starts
        :return:
        """
        server = self.openresty
        server.install(reset=True)
        server.configure()
        website = server.get_from_port(8080)
        static_location = locations.locations_static.new()
        static_location.name = "static"
        static_location.path_url = "/"
        path = j.clients.git.getContentPathFromURLorPath(self.incubaid, branch=self.branch, pull=True)
        static_location.path_location = path
        static_location.use_jumpscale_weblibs = True
        website.path = path
        locations.configure()
        website.configure()

    def start(self):
        """
        called when the 3bot starts
        :return:
        """
        self.prepare()
    def stop(self):
        """
        called when the 3bot stops
        :return:
        """
        pass

    def uninstall(self):
        """
        called when the package is no longer needed and will be removed from the threebot
        :return:
        """
        pass
