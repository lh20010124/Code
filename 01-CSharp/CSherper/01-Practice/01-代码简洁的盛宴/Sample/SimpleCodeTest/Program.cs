// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

A aa = new A();
aa.B = 2;
System.Console.WriteLine("aa.B = " + aa.B);
System.Console.WriteLine("aa.Cnt = " + aa.Cnt);
System.Console.WriteLine("aa.Cnt1 = " + aa.Cnt1);
System.Console.WriteLine("----------------");

A bb = new A { B = 5, Cnt = 3, Cnt1 = 10};
System.Console.WriteLine("bb.B = " + bb.B);
System.Console.WriteLine("bb.Cnt = " + bb.Cnt);
System.Console.WriteLine("bb.Cnt1 = " + bb.Cnt1);
System.Console.WriteLine("----------------");

// 内插字符串
System.Console.WriteLine($"bb.B = {bb.B}");
System.Console.WriteLine($"bb.Cnt = {bb.Cnt:00}");  
System.Console.WriteLine($"bb.Cnt1 = {bb.Cnt1:0.000}");
System.Console.WriteLine("----------------");

System.Console.WriteLine(string.Format("from Format bb.B = {0}, bb.Cnt = {1}, bb.Cnt1 = {2}", bb.B, bb.Cnt.ToString("00"), bb.Cnt1.ToString("0.000")));

// 异步

// HttpClient httpClient = new();
// System.Console.WriteLine("任务开始前" + DateTime.Now.ToString("ss.ffff"));
// var Ta = httpClient.GetAsync("http://www.baidu.com");
// var Tb = httpClient.GetAsync("http://www.bing.com");
// System.Console.WriteLine("任务开始" + DateTime.Now.ToString("ss.ffff"));
// var resa = await Ta;
// System.Console.WriteLine("a任务结束" + DateTime.Now.ToString("ss.ffff"));
// var resb = await Tb;
// System.Console.WriteLine("b任务结束" + DateTime.Now.ToString("ss.ffff"));
// await Task.Delay(1000);
// System.Console.WriteLine(await resa.Content.ReadAsStringAsync());
// await Task.Delay(1000);
// System.Console.WriteLine(await resb.Content.ReadAsStringAsync());

// LINQ
int[] array = new[] { 1, 7, 6, 7, 2, 4, 5, 7, 9 };
for (int i = 0; i < array.Length; i++)
{
    if (array[i] > 3)
    {
        System.Console.WriteLine(array[i]);
    }
}
System.Console.WriteLine("----");
array.Where(s => s > 3).ToList().ForEach(System.Console.WriteLine);

// 自动实现属性
class A
{
    private int _cnt = 4;

    public int B;

    public int Cnt
    {
        get { return _cnt; }
        set { _cnt = value; }
    }

    public double Cnt1 { get; set; } = 3;
}
