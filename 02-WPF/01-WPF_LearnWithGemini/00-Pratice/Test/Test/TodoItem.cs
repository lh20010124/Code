using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace Test
{
    public class TodoItem : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler? PropertyChanged;
        protected void OnPropertyChanged([CallerMemberName] string name = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }

        private string _content;

        public string Content
        {
            get { return _content; }
            set { _content = value; OnPropertyChanged(); }
        }
        private bool _IsDone;

        public bool IsDone
        {
            get { return _IsDone; }
            set { _IsDone = value; OnPropertyChanged(); }
        }
        private int _priority;

        public int Priority
        {
            get { return _priority; }
            set { _priority = value; OnPropertyChanged(); }
        }
        public Guid ID { get; set; } = Guid.NewGuid();
    }
}
