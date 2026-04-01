using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;
using Test;

public class MainViewModel : INotifyPropertyChanged
{
    // 1. 任务集合：绑定到 ListBox 的 ItemsSource
    public ObservableCollection<TodoItem> TodoList { get; set; }

    // 2. 绑定输入框的属性
    private string _newTaskContent;
    public string NewTaskContent
    {
        get => _newTaskContent;
        set { _newTaskContent = value; OnPropertyChanged(); }
    }

    // 3. 命令定义
    public ICommand AddTaskCommand { get; }
    public ICommand DeleteTaskCommand { get; }

    public MainViewModel()
    {
        // 初始化数据
        TodoList = new ObservableCollection<TodoItem>();

        // 绑定命令逻辑
        AddTaskCommand = new RelayCommand(obj => AddTask());
        DeleteTaskCommand = new RelayCommand(obj => DeleteTask(obj));

        // 测试数据
        TodoList.Add(new TodoItem { Content = "复习 WPF 数据绑定", Priority = 2 });
    }

    private void AddTask()
    {
        if (!string.IsNullOrWhiteSpace(NewTaskContent))
        {
            TodoList.Add(new TodoItem
            {
                Content = NewTaskContent,
                Priority = 1
            });
            NewTaskContent = string.Empty; // 添加完成后清空输入框
        }
    }

    private void DeleteTask(object parameter)
    {
        // 这里的 parameter 是通过 CommandParameter 传进来的 TodoItem 对象
        if (parameter is TodoItem task)
        {
            TodoList.Remove(task);
        }
    }

    // 实现 PropertyChanged
    public event PropertyChangedEventHandler PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string name = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}