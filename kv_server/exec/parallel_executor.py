import concurrent.futures


class ParallelExecutor(object):

    @classmethod
    def execute(self, lazy_functions):
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for lazy_function in lazy_functions:
                future = executor.submit(lazy_function)
                futures.append(future)
            for future in futures:
                result = future.result()
                results.append(result)
        return results
