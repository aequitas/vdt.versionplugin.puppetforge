vdt.versionplugin.puppetmodule
==============================

Plugin for https://github.com/devopsconsulting/vdt.version

This plugin can be used to create a debian package from a puppet module.
The module will be installed in the default module dir: ``/etc/puppet/modules``.

This plugin uses FPM. See also http://gofedora.wordpress.com/2012/04/19/easy-package-management-with-fpm/

FPM should be install as a gem using rubygems : 

    gem install fpm

After that you can use this plugin the following way : 

    version --plugin puppetmodule -t <package type> --maintainer <maintainer>

