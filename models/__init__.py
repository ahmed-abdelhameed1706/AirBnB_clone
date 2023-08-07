#!/usr/bin/python3
"""
updating init to create a unique file storage
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
