<p align="center">
  <img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" alt="seven logo" />
</p>

<h1 align="center">seven SMS &amp; Voice for StackStorm</h1>

<p align="center">
  Integration pack for <a href="https://stackstorm.com/">StackStorm</a> that sends SMS and places text-to-speech calls via the seven gateway.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-teal.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/StackStorm-pack-blue" alt="StackStorm pack" />
  <img src="https://img.shields.io/badge/Python-3-yellow" alt="Python 3" />
</p>

---

## Actions

| Action | Description |
|--------|-------------|
| `seven.send_sms` | Send an SMS. Multiple recipients can be comma-separated. |
| `seven.send_voice` | Place a text-to-speech voice call. |

## Prerequisites

- A [StackStorm](https://stackstorm.com/) installation
- A [seven account](https://www.seven.io/) with API key ([How to get your API key](https://help.seven.io/en/developer/where-do-i-find-my-api-key))

## Installation

```bash
st2 pack install https://github.com/seven-io/StackStorm
```

## Configuration

Copy the sample config and edit it:

```bash
cp seven.yaml.dist /opt/stackstorm/configs/seven.yaml
```

| Field | Description |
|-------|-------------|
| `api_key` | Your seven API key |

Dynamic [datastore values](https://docs.stackstorm.com/reference/pack_configs.html) can be referenced as well.

After editing, reload the config:

```bash
st2ctl reload --register-configs
```

## Usage

### Send SMS

```bash
st2 run seven.send_sms \
    to="01716992343,491625453093" \
    text=HI2U \
    from=StackStorm \
    flash=true \
    performance_tracking=true \
    label=CustomLabel \
    foreign_id=ForeignID \
    delay="2021-12-30 12:00"
```

### Send Voice

```bash
st2 run seven.send_voice \
    to=+491716992343 \
    text='Dear sir or madam' \
    from=+13134378004 \
    xml=false
```

## Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/) or [open an issue](https://github.com/seven-io/StackStorm/issues).

## License

[MIT](LICENSE)
