using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Sample2
{
    public class MainViewModel
    {
        public ObservableCollection<TodoItem> TodoLists { get; } = new ObservableCollection<TodoItem>
        {
            new TodoItem { Title = "Buy groceries", IsCompleted = false},
            new TodoItem { Title = "Walk the dog", IsCompleted = false},
            new TodoItem { Title = "Finish project", IsCompleted = false}
        };
        public ICommand AddTaskCommand { get; }
        public ICommand DeleteTaskCommand { get; }
        public MainViewModel()
        {
            AddTaskCommand = new RelayCommand(obj => TodoLists.Add(new TodoItem { Title = "New Task"}));
            DeleteTaskCommand = new RelayCommand(obj =>
            {
                if (obj is TodoItem item)
                {
                    TodoLists.Remove(item);
                }   
            });
        }
    }
}
