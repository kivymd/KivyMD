# Copyright (c) 2019-2021 Artem Bulgakov
#
# This file is distributed under the terms of the same license,
# as the Kivy framework.

import argparse
import sys


class ArgumentParserWithHelp(argparse.ArgumentParser):
    def parse_args(self, args=None, namespace=None):
        # Add help when no arguments specified
        if not args and not len(sys.argv) > 1:
            self.print_help()
            self.exit(1)
        return super().parse_args(args, namespace)

    def error(self, message):
        # Add full help on error
        self.print_help()
        self.exit(2, f"\nError: {message}\n")

    def format_help(self):
        # Add subparsers usage and help to full help text
        formatter = self._get_formatter()

        # Get subparsers
        subparsers_actions = [
            action
            for action in self._actions
            if isinstance(action, argparse._SubParsersAction)
        ]

        # Description
        formatter.add_text(self.description)

        # Usage
        formatter.add_usage(
            self.usage,
            self._actions,
            self._mutually_exclusive_groups,
            prefix="Usage:\n",
        )

        # Subparsers usage
        for subparsers_action in subparsers_actions:
            for choice, subparser in subparsers_action.choices.items():
                formatter.add_usage(
                    subparser.usage,
                    subparser._actions,
                    subparser._mutually_exclusive_groups,
                    prefix="",
                )

        # Positionals, optionals and user-defined groups
        for action_group in self._action_groups:
            if not any(
                [
                    action in subparsers_actions
                    for action in action_group._group_actions
                ]
            ):
                formatter.start_section(action_group.title)
                formatter.add_text(action_group.description)
                formatter.add_arguments(action_group._group_actions)
                formatter.end_section()
            else:
                # Process subparsers differently
                # Just show list of choices
                formatter.start_section(action_group.title)
                # formatter.add_text(action_group.description)
                for action in action_group._group_actions:
                    for choice in action.choices:
                        formatter.add_text(choice)
                formatter.end_section()

        # Subparsers help
        for subparsers_action in subparsers_actions:
            for choice, subparser in subparsers_action.choices.items():
                formatter.start_section(choice)
                for action_group in subparser._action_groups:
                    formatter.start_section(action_group.title)
                    formatter.add_text(action_group.description)
                    formatter.add_arguments(action_group._group_actions)
                    formatter.end_section()
                formatter.end_section()

        # Epilog
        formatter.add_text(self.epilog)

        # Determine help from format above
        return formatter.format_help()
