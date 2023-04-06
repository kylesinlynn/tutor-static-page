from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env",
        '"MKTG_URL_LINK_MAP": {"instructor":"instructor.html"}'
    )
)
