[![Test deployment](https://github.com/GeekOops/geekoops-grafana/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-grafana/actions/workflows/CI.yml)

# geekoops-grafana

Easy ansible role for setup of `grafana` with a custom backend. Currently only `influxdb` is supported. This ansible role works with

- openSUSE Leap 15.2


## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
|`config_firewall`|Configure firewalld | false |
|`firewall_zone`| Firewall zone which should be configured | public |
|`open_grafana_port`| If the role should open the grafana port | false |
|`grafana_port` | Port for grafana | 3000 |
|`influxdb`| Configure `influxdb` | false |
|`influxdb_port`| InfluxDB port, if enabled | 8086 |
|`influxdb_bind` | InfluxDB address to bind to, if enabled | "" |
|`open_influxdb_port` | Open the InfluxDB port, if `config_firewall` is true | false |
|`influxdb_collectd` | Configure `collecd` for InfluxDB | false |
|`influxdb_collectd_database` | Name of the `collectd` database for InfluxDB, if enabled | "collectd" |
|`influxdb_collectd_port` | `collectd` port to be used, if enabled | 25826 |
|`influxdb_collectd_bind` | `collectd` bind address, if enabled | "" |
|`open_collectd_port` | Open the `collectd` port, if `config_firewall` is true | false |


## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-grafana }

And a more extended example, configure `grafana` with `influxdb` and enable `collectd`

    - hosts: jellyfish
      roles:
         - role: geekoops-grafana
           vars:
             config_firewall: true
             firewall_zone: "public"
             open_grafana_port: true
             influxdb: true
             influxdb_collectd: true
             open_influxdb_port: true
             open_collectd_port: true


## License

MIT

## Author Information

phoenix

Have a lot of fun!
