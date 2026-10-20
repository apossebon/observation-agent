import textwrap
from pathlib import Path

import pytest

MSG = """\
Message-ID: <{mid}.JavaMail.evans@thyme>
Date: {date}
From: {sender}
To: {to}
Subject: {subject}
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
X-From: {sender}
X-Folder: \\Test\\Inbox

{body}
"""


def write_msg(root: Path, rel: str, **kw):
    defaults = dict(mid="1", date="Mon, 29 Oct 2001 18:59:07 -0800 (PST)", sender="a@enron.com",
                    to="b@enron.com", subject="Test", body="Hello there.")
    defaults.update(kw)
    p = root / (rel + ".")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(MSG.format(**defaults), encoding="utf-8")
    return p


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    root = tmp_path / "corpus"
    write_msg(root, "giron-d/sent/1", mid="1", subject="Calpine Daily Gas Nomination",
              body="Confirmed on my end.  Same volumes as yesterday, no changes to the path.\n\nDG")
    write_msg(root, "farmer-d/logistics/2", mid="2", subject="RE: Calpine Daily Gas Nomination",
              date="Tue, 30 Oct 2001 09:00:00 -0800 (PST)",
              body="Thanks.\n\n-----Original Message-----\nFrom: Giron, Darron\nSent: Monday\n\nConfirmed on my end.")
    # exact duplicate of message 1 stored in another mailbox with a different Message-ID
    write_msg(root, "lokay-m/inbox/3", mid="3", subject="Calpine Daily Gas Nomination",
              body="Confirmed on my end.  Same volumes as yesterday, no changes to the path.\n\nDG")
    write_msg(root, "lokay-m/inbox/4", mid="4", date="Tues, 32 Febuary 2001 25:61:00", subject="Lunch",
              body="Lunch at noon?")
    write_msg(root, "lokay-m/inbox/5", mid="5", date="Wed, 12 Mar 2031 08:14:00 -0600 (CST)", subject="",
              body="Future mail with no subject line but enough text to quote.")
    return root
