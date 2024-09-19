# apache

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/apache)
[![General Workflow](https://github.com/rolehippie/apache/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/apache/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/apache/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/apache/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/apache/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/apache/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/apache)](https://github.com/rolehippie/apache/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.apache-blue)](https://galaxy.ansible.com/rolehippie/apache)

Ansible role to install and configure an Apache webserver.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [apache_default_server_listen](#apache_default_server_listen)
  - [apache_default_server_name](#apache_default_server_name)
  - [apache_error_pages](#apache_error_pages)
  - [apache_exporter_args](#apache_exporter_args)
  - [apache_exporter_download](#apache_exporter_download)
  - [apache_exporter_enabled](#apache_exporter_enabled)
  - [apache_exporter_scrape_uri](#apache_exporter_scrape_uri)
  - [apache_exporter_version](#apache_exporter_version)
  - [apache_extra_modules](#apache_extra_modules)
  - [apache_extra_packages](#apache_extra_packages)
  - [apache_general_modules](#apache_general_modules)
  - [apache_general_packages](#apache_general_packages)
  - [apache_index_content](#apache_index_content)
  - [apache_keep_index](#apache_keep_index)
  - [apache_language_priority](#apache_language_priority)
  - [apache_listen](#apache_listen)
  - [apache_server_admin](#apache_server_admin)
  - [apache_server_signature](#apache_server_signature)
  - [apache_server_tokens](#apache_server_tokens)
  - [apache_trace_enable](#apache_trace_enable)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### apache_default_server_listen

Listening address of default vhost

#### Default value

```YAML
apache_default_server_listen: 0.0.0.0:80
```

### apache_default_server_name

Optional default server name

#### Default value

```YAML
apache_default_server_name:
```

#### Example usage

```YAML
apache_default_server_name: server.example.com
```

### apache_error_pages

Path to error page files

#### Default value

```YAML
apache_error_pages: error
```

### apache_exporter_args

Optional list of additional arguments for the apache exporter

#### Default value

```YAML
apache_exporter_args: []
```

### apache_exporter_download

URL to the apache exporter to install

#### Default value

```YAML
apache_exporter_download: https://github.com/Lusitaniae/apache_exporter/releases/download/v{{
  apache_exporter_version }}/apache_exporter-{{ apache_exporter_version }}.linux-amd64.tar.gz
```

### apache_exporter_enabled

Enable the installation of the apache exporter

#### Default value

```YAML
apache_exporter_enabled: true
```

### apache_exporter_scrape_uri

Scrape URI of the exporter

#### Default value

```YAML
apache_exporter_scrape_uri: http://{{ 'localhost' if apache_default_server_listen
  == '0.0.0.0:80' else apache_default_server_listen }}/server-status/?auto
```

### apache_exporter_version

Version of the apache exporter to install

#### Default value

```YAML
apache_exporter_version: 1.0.9
```

### apache_extra_modules

List of additional modules to enable

#### Default value

```YAML
apache_extra_modules: []
```

#### Example usage

```YAML
apache_extra_modules:
  - proxy
  - name: ssl
    state: present
  - name: foobar
    state: absent
```

### apache_extra_packages

List of additional packages to install

#### Default value

```YAML
apache_extra_packages: []
```

### apache_general_modules

List of modules to enable

#### Default value

```YAML
apache_general_modules:
  - name: rpaf
    state: present
  - name: ssl
    state: present
  - name: rewrite
    state: present
  - name: include
    state: present
  - name: alias
    state: present
  - name: negotiation
    state: present
```

#### Example usage

```YAML
apache_general_modules:
  - proxy
  - name: ssl
    state: present
  - name: foobar
    state: absent
```

### apache_general_packages

List of packages to install

#### Default value

```YAML
apache_general_packages:
  - apache2
  - apachetop
  - libapache2-mod-rpaf
```

### apache_index_content

Optional content for index page

#### Default value

```YAML
apache_index_content:
```

### apache_keep_index

Keep an empty index page

#### Default value

```YAML
apache_keep_index: true
```

### apache_language_priority

List of language priorities for error pages

#### Default value

```YAML
apache_language_priority:
  - de
  - en
  - cs
  - es
  - fr
  - it
  - nl
  - sv
  - pt-br
  - ro
```

### apache_listen

List of ports to listen to

#### Default value

```YAML
apache_listen:
  - 80
```

#### Example usage

```YAML
apache_listen:
  - 80
  - 127.0.0.1:8080
```

### apache_server_admin

Email address of server admin

#### Default value

```YAML
apache_server_admin: hostmaster@localhost
```

### apache_server_signature

Display server version and virtual host name

#### Default value

```YAML
apache_server_signature: Off
```

### apache_server_tokens

What you return as the server HTTP response

#### Default value

```YAML
apache_server_tokens: Prod
```

### apache_trace_enable

Allow TRACE method for the webserver

#### Default value

```YAML
apache_trace_enable: Off
```

## Discovered Tags

**_apache_**

**_apache-exporter_**


## Dependencies

- [community.general](https://github.com/ansible-collections/community.general)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
