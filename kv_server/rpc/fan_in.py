import bisect


class FanIn(object):

    @classmethod
    def merge_lists_sorted(cls, lists):
        merged_list = []
        for l in lists:
            for e in l:
                bisect.insort_right(merged_list, e)
        return merged_list
