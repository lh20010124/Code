using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Sample1
{
    public class MainViewModel : INotifyPropertyChanged
    {
        private string _userName = "Gemini";
        public event PropertyChangedEventHandler PropertyChanged;

        public string UserName
        {
            get => _userName;
            set
            {
                if (_userName != value)
                {
                    _userName = value;
                    OnPropertyChanged(); // 广播：通知 UI 刷新
                }
            }
        }

        // 命令：用于绑定到按钮
        public ICommand ChangeNameCommand { get; }
        public ICommand ClearNameCommand { get; }

        public MainViewModel()
        {
            ChangeNameCommand = new RelayCommand(obj => UserName = "数据已更新！");
            ClearNameCommand = new RelayCommand(obj => UserName = "");
        }

        protected void OnPropertyChanged([CallerMemberName] string name = null)
            => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}
