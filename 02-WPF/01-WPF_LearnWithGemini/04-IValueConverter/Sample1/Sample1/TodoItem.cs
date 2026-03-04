using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace Sample1
{
    public class TodoItem : INotifyPropertyChanged
    {
        public string Title { get; set; }

        private bool _isCompleted;
        public bool IsCompleted
        {
            get => _isCompleted;
            set
            {
                if (_isCompleted != value)
                {
                    _isCompleted = value;
                    // 通知界面：IsCompleted 变了，请刷新相关 UI
                    OnPropertyChanged();
                }
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;
        protected void OnPropertyChanged([CallerMemberName] string name = null)
            => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}   