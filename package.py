from Jumpscale import j

class Package(j.baseclasses.threebot_package):

    def start(self):
        server = self.openresty
        server.configure()
        for port in [80, 443]:
            website = server.get_from_port(port)
            website.domain = "incubaid.com"
            locations = website.locations.get(f"incubaid_locations_{port}")

            website_location = locations.locations_static.new()
            website_location.name = "incubaidwebsite"
            website_location.path_url = "/"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
