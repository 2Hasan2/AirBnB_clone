#!/usr/bin/python3
class Color:
    """Usage: f"{Color.ColorName}Text{Color.End}" """
    Error = '\033[91m'
    Success = '\033[92m'
    Prompt = '\033[94m'
    End = '\033[0m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    Purple = '\033[95m'
    Warning = '\033[93m'

    def disable(self):
        """Disable color"""
        self.Error = ''
        self.Success = ''
        self.End = ''
        self.Bold = ''
        self.Underline = ''
        self.Purple = ''
        self.Warning = ''
        self.Prompt = ''

    def enable(self):
        """Enable color"""
        self.Error = '\033[91m'
        self.Success = '\033[92m'
        self.End = '\033[0m'
        self.Bold = '\033[1m'
        self.Underline = '\033[4m'
        self.Purple = '\033[95m'
        self.Warning = '\033[93m'
        self.Prompt = '\033[94m'
