

using System.Collections.ObjectModel;
using System.Windows.Input;

namespace Sample3
{
    public class MainViewModel
    {
        public ObservableCollection<TodoItem> TodoList { get; set; } = new ObservableCollection<TodoItem>() { };
        public ICommand AddTaskCommand { get; set; }
        public ICommand DeleteTaskCommand { get; set; }
        public MainViewModel()
        {
            TodoList.Add(new TodoItem { Title = "1", IsCompleted = false, Priority = 1 });
            AddTaskCommand = new RelayCommand(_ =>
            {
                var newTask = new TodoItem { Title = $"Task {TodoList.Count + 1}", IsCompleted = false, Priority = 1 };
                TodoList.Add(newTask);
            });
            DeleteTaskCommand = new RelayCommand(task =>
                {
                    if (task is TodoItem todo)
                    {
                        TodoList.Remove(todo);
                    }
                });
        }
    }
}
