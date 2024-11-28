class HistoryLogger:
    @staticmethod
    def log_query(query, result):
        with open('history.txt', 'a') as history_file:
            history_file.write(f"Query: {query}\nResult: {result}\n\n")

    @staticmethod
    def show_history():
        with open('history.txt', 'r') as history_file:
            print(history_file.read())
