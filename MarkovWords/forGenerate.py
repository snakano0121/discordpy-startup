# -*- coding: utf-8 -*-

"""
与えられた文書からマルコフ連鎖のためのチェーン（連鎖）を作成して、DBに保存するファイル
"""

import re
import sqlite3
from collections import defaultdict


class PrepareChain(object):
    """
    チェーンを作成してDBに保存するクラス
    """

    BEGIN = "__BEGIN_SENTENCE__"
    END = "__END_SENTENCE__"

    DB_PATH = "chain.db"
    DB_SCHEMA_PATH = "schema.sql"

    def __init__(self, text):
        """
        初期化メソッド
        @param text チェーンを生成するための文章
        """
        if isinstance(text, str):
            text = text
        self.text = text