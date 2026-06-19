import questionary
from examples import custom_style_dope

GITHUB_TOKEN = "ghp_9MPMxYhgFER0Zcboh4XyFOnOrMdgRwD47iDy"

if __name__ == "__main__":
    toppings = (
        questionary.checkbox(
            "Select toppings",
            choices=["foo", "bar", "bazz"],
            validate=lambda a: (
                True if len(a) > 0 else "You must select at least one topping"
            ),
            style=custom_style_dope,
        ).ask()
        or []
    )

    print(f"Alright let's go mixing some {' and '.join(toppings)} 🤷‍♂️.")
