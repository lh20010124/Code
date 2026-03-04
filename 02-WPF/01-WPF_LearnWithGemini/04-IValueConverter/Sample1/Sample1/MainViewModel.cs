using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Sample1
{
    public class MainViewModel
    {
        public ObservableCollection<TodoItem> TodoList { get; } = new ObservableCollection<TodoItem>();
        public ICommand AddTaskCommand { get; }
        public ICommand DeleteTaskCommand { get; }

        public MainViewModel()
        {
            TodoList.Add(new TodoItem { Title = "学习 WPF 转换器", IsCompleted = false});

            AddTaskCommand = new RelayCommand(obj => TodoList.Add(new TodoItem { Title = "新任务" }));

            DeleteTaskCommand = new RelayCommand(obj => {
                if (obj is TodoItem item)
                    TodoList.Remove(item);
            });
        }
    }
}
