
hello = ['   mAce', 'Whip', "the way"]


def normalize_space(s):
    """Return s stripped of leading/trailing whitespace
    and with internal runs of whitespace replaced by a single SPACE"""
    # This should be a str method :-(
    return ' '.join(s.split()).lower()


replacement = [normalize_space(i) for i in hello]

print(replacement)
