from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

completer = NestedCompleter.from_nested_dict({
    "show": {
        "version": None,
        "clock": None,
        "ip": {
            "interface": {"brief"}
        }
    },
    "exit": None,
})

def generate_prompt(user):
    initial_prompt="#"
    final_prompt = initial_prompt + "{user}"
    return final_prompt

