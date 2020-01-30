from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    """
    JSX> cl = j.servers.threebot.local_start_zerobot(background=False)
    JSX> cl = j.clients.gedis.get("abc", port=8901, package_name="zerobot.packagemanager")
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/Incubaid/www_incubaid/tree/3bot")
    """
    DOMAIN = "www.incubaid.com"
    def start(self):
        server = self.openresty
        server.configure()
        website_incubaid = server.websites.get("www_incubaid_com")
        website_incubaid.domain = self.DOMAIN
        website_incubaid.port = 80
        website_incubaid.ssl = False

        websites = [server.get_from_port(80), server.get_from_port(443), website_incubaid]
        for website in websites:
            locations = website.locations.get(f"3bot_locations_{website.name}")

            website_location = locations.locations_static.new()
            website_location.name = "incubaid_website"
            website_location.path_url = "/" if website.domain == self.DOMAIN else "/incubaid_com"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
