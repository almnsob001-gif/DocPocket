import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';

void main() {
  runApp(const MedCalcHubApp());
}

class MedCalcHubApp extends StatelessWidget {
  const MedCalcHubApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MedCalc Hub',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
      ),
      home: const SplashScreen(),
    );
  }
}

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});
  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    _checkFirstRun();
  }

  Future<void> _checkFirstRun() async {
    final prefs = await SharedPreferences.getInstance();
    final seen = prefs.getBool('disclaimer_seen') ?? false;
    if (mounted) {
      Navigator.of(context).pushReplacement(MaterialPageRoute(
        builder: (_) => seen ? const HomeScreen() : const GetStartedScreen(),
      ));
    }
  }

  @override
  Widget build(BuildContext context) {
    return const Scaffold(body: Center(child: CircularProgressIndicator()));
  }
}

class GetStartedScreen extends StatelessWidget {
  const GetStartedScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.medical_services, size: 100, color: Theme.of(context).colorScheme.primary),
            const SizedBox(height: 24),
            const Text('MedCalc Hub', style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            const Text('Your personal medical companion', style: TextStyle(fontSize: 16, color: Colors.grey)),
            const SizedBox(height: 48),
            FilledButton(
              onPressed: () => Navigator.of(context).pushReplacement(
                MaterialPageRoute(builder: (_) => const DisclaimerScreen()),
              ),
              style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 52)),
              child: const Text('GET STARTED', style: TextStyle(fontSize: 16)),
            ),
          ],
        ),
      ),
    );
  }
}

class DisclaimerScreen extends StatelessWidget {
  const DisclaimerScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Disclaimer')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Icon(Icons.warning_amber_rounded, size: 60, color: Colors.orange),
            const SizedBox(height: 16),
            const Text('Medical Disclaimer', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            const Text(
              'This application (MedCalc Hub) is an educational tool and NOT a substitute for professional medical advice, diagnosis, or treatment.\n\n'
              'Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.\n\n'
              'In case of emergency, call your local emergency number immediately.\n\n'
              'By continuing, you agree to use this application at your own risk.',
              style: TextStyle(fontSize: 15, height: 1.5),
            ),
            const SizedBox(height: 32),
            FilledButton(
              onPressed: () async {
                final prefs = await SharedPreferences.getInstance();
                await prefs.setBool('disclaimer_seen', true);
                if (context.mounted) {
                  Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const HomeScreen()));
                }
              },
              style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 52)),
              child: const Text('I AGREE AND CONTINUE'),
            ),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final features = [
      {'icon': Icons.calculate, 'title': 'BMI Calculator', 'color': Colors.deepPurple, 'page': const BMIScreen()},
      {'icon': Icons.favorite, 'title': 'Blood Pressure', 'color': Colors.red, 'page': const BPScreen()},
      {'icon': Icons.water_drop, 'title': 'Blood Sugar', 'color': Colors.blue, 'page': const SugarScreen()},
      {'icon': Icons.medication, 'title': 'Medications', 'color': Colors.green, 'page': const MedsScreen()},
      {'icon': Icons.local_fire_department, 'title': 'Calories', 'color': Colors.orange, 'page': const CalorieScreen()},
    ];
    return Scaffold(
      appBar: AppBar(
        title: const Text('MedCalc Hub'),
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Colors.white,
      ),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: features.length,
        separatorBuilder: (_, __) => const SizedBox(height: 12),
        itemBuilder: (context, i) {
          final f = features[i];
          return Card(
            elevation: 2,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            child: ListTile(
              contentPadding: const EdgeInsets.all(16),
              leading: Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: f['color'] as Color, borderRadius: BorderRadius.circular(12)),
                child: Icon(f['icon'] as IconData, color: Colors.white, size: 28),
              ),
              title: Text(f['title'] as String, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => f['page'] as Widget)),
            ),
          );
        },
      ),
    );
  }
}

class BMIScreen extends StatefulWidget {
  const BMIScreen({super.key});
  @override
  State<BMIScreen> createState() => _BMIScreenState();
}

class _BMIScreenState extends State<BMIScreen> {
  final h = TextEditingController();
  final w = TextEditingController();
  double? bmi;
  String cat = '';
  Color color = Colors.grey;

  void calc() {
    final hv = double.tryParse(h.text);
    final wv = double.tryParse(w.text);
    if (hv == null || wv == null || hv <= 0 || wv <= 0) return;
    final b = wv / ((hv / 100) * (hv / 100));
    setState(() {
      bmi = b;
      if (b < 18.5) { cat = 'Underweight'; color = Colors.blue; }
      else if (b < 25) { cat = 'Normal'; color = Colors.green; }
      else if (b < 30) { cat = 'Overweight'; color = Colors.orange; }
      else { cat = 'Obese'; color = Colors.red; }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('BMI Calculator')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(children: [
          TextField(controller: h, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Height (cm)', border: OutlineInputBorder())),
          const SizedBox(height: 12),
          TextField(controller: w, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Weight (kg)', border: OutlineInputBorder())),
          const SizedBox(height: 20),
          FilledButton(onPressed: calc, style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 50)), child: const Text('CALCULATE')),
          const SizedBox(height: 20),
          if (bmi != null)
            Card(
              color: color.withOpacity(0.15),
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(children: [
                  Text(bmi!.toStringAsFixed(1), style: TextStyle(fontSize: 56, fontWeight: FontWeight.bold, color: color)),
                  Text(cat, style: TextStyle(fontSize: 20, color: color, fontWeight: FontWeight.bold)),
                ]),
              ),
            ),
        ]),
      ),
    );
  }
}

class BPScreen extends StatefulWidget {
  const BPScreen({super.key});
  @override
  State<BPScreen> createState() => _BPScreenState();
}

class _BPScreenState extends State<BPScreen> {
  final sys = TextEditingController();
  final dia = TextEditingController();
  List<Map<String, dynamic>> readings = [];

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final prefs = await SharedPreferences.getInstance();
    final data = prefs.getString('bp_data');
    if (data != null) setState(() => readings = List<Map<String, dynamic>>.from(jsonDecode(data)));
  }

  Future<void> _save() async {
    final s = int.tryParse(sys.text);
    final d = int.tryParse(dia.text);
    if (s == null || d == null) return;
    setState(() {
      readings.insert(0, {'sys': s, 'dia': d, 'date': DateTime.now().toString().substring(0, 16)});
    });
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('bp_data', jsonEncode(readings));
    sys.clear(); dia.clear();
  }

  Color _color(int s, int d) {
    if (s < 120 && d < 80) return Colors.green;
    if (s < 140) return Colors.orange;
    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Blood Pressure')),
      body: Column(children: [
        Padding(
          padding: const EdgeInsets.all(16),
          child: Row(children: [
            Expanded(child: TextField(controller: sys, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Systolic', border: OutlineInputBorder()))),
            const SizedBox(width: 8),
            Expanded(child: TextField(controller: dia, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Diastolic', border: OutlineInputBorder()))),
          ]),
        ),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: FilledButton(onPressed: _save, style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 48)), child: const Text('SAVE READING')),
        ),
        const SizedBox(height: 16),
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: readings.length,
            itemBuilder: (context, i) {
              final r = readings[i];
              return Card(
                child: ListTile(
                  title: Text('${r['sys']}/${r['dia']} mmHg', style: TextStyle(fontWeight: FontWeight.bold, color: _color(r['sys'], r['dia']))),
                  subtitle: Text(r['date']),
                ),
              );
            },
          ),
        ),
      ]),
    );
  }
}

class SugarScreen extends StatefulWidget {
  const SugarScreen({super.key});
  @override
  State<SugarScreen> createState() => _SugarScreenState();
}

class _SugarScreenState extends State<SugarScreen> {
  final ctrl = TextEditingController();
  String type = 'Fasting';
  List<Map<String, dynamic>> readings = [];

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final prefs = await SharedPreferences.getInstance();
    final data = prefs.getString('sugar_data');
    if (data != null) setState(() => readings = List<Map<String, dynamic>>.from(jsonDecode(data)));
  }

  Future<void> _save() async {
    final g = double.tryParse(ctrl.text);
    if (g == null) return;
    setState(() {
      readings.insert(0, {'g': g, 'type': type, 'date': DateTime.now().toString().substring(0, 16)});
    });
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('sugar_data', jsonEncode(readings));
    ctrl.clear();
  }

  Color _color(double g) {
    if (g < 70) return Colors.blue;
    if (g < 140) return Colors.green;
    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Blood Sugar')),
      body: Column(children: [
        Padding(
          padding: const EdgeInsets.all(16),
          child: Row(children: [
            Expanded(child: TextField(controller: ctrl, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Glucose (mg/dL)', border: OutlineInputBorder()))),
            const SizedBox(width: 8),
            DropdownButton<String>(
              value: type,
              items: ['Fasting', 'Post-meal', 'Random'].map((t) => DropdownMenuItem(value: t, child: Text(t))).toList(),
              onChanged: (v) => setState(() => type = v!),
            ),
          ]),
        ),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: FilledButton(onPressed: _save, style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 48)), child: const Text('SAVE READING')),
        ),
        const SizedBox(height: 16),
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: readings.length,
            itemBuilder: (context, i) {
              final r = readings[i];
              return Card(
                child: ListTile(
                  title: Text('${r['g']} mg/dL (${r['type']})', style: TextStyle(fontWeight: FontWeight.bold, color: _color(r['g']))),
                  subtitle: Text(r['date']),
                ),
              );
            },
          ),
        ),
      ]),
    );
  }
}

class MedsScreen extends StatefulWidget {
  const MedsScreen({super.key});
  @override
  State<MedsScreen> createState() => _MedsScreenState();
}

class _MedsScreenState extends State<MedsScreen> {
  final name = TextEditingController();
  final dose = TextEditingController();
  TimeOfDay? time;
  List<Map<String, dynamic>> meds = [];

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final prefs = await SharedPreferences.getInstance();
    final data = prefs.getString('meds_data');
    if (data != null) setState(() => meds = List<Map<String, dynamic>>.from(jsonDecode(data)));
  }

  Future<void> _pickTime() async {
    final t = await showTimePicker(context: context, initialTime: TimeOfDay.now());
    if (t != null) setState(() => time = t);
  }

  Future<void> _add() async {
    if (name.text.isEmpty || dose.text.isEmpty || time == null) return;
    setState(() {
      meds.insert(0, {'name': name.text, 'dose': dose.text, 'time': '${time!.hour.toString().padLeft(2, '0')}:${time!.minute.toString().padLeft(2, '0')}'});
    });
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('meds_data', jsonEncode(meds));
    name.clear(); dose.clear(); setState(() => time = null);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Medications')),
      body: Column(children: [
        Padding(
          padding: const EdgeInsets.all(16),
          child: Column(children: [
            TextField(controller: name, decoration: const InputDecoration(labelText: 'Medication name', border: OutlineInputBorder())),
            const SizedBox(height: 8),
            TextField(controller: dose, decoration: const InputDecoration(labelText: 'Dose (e.g. 500mg)', border: OutlineInputBorder())),
            const SizedBox(height: 8),
            Row(children: [
              Expanded(child: OutlinedButton(onPressed: _pickTime, child: Text(time == null ? 'Pick Time' : 'Time: ${time!.format(context)}'))),
              const SizedBox(width: 8),
              FilledButton(onPressed: _add, child: const Text('ADD')),
            ]),
          ]),
        ),
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: meds.length,
            itemBuilder: (context, i) {
              final m = meds[i];
              return Card(
                child: ListTile(
                  leading: const Icon(Icons.medication, color: Colors.green),
                  title: Text(m['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text('${m['dose']} • ${m['time']}'),
                ),
              );
            },
          ),
        ),
      ]),
    );
  }
}

class CalorieScreen extends StatefulWidget {
  const CalorieScreen({super.key});
  @override
  State<CalorieScreen> createState() => _CalorieScreenState();
}

class _CalorieScreenState extends State<CalorieScreen> {
  final age = TextEditingController();
  final h = TextEditingController();
  final w = TextEditingController();
  bool male = true;
  double mult = 1.2;
  int? result;

  void _calc() {
    final a = int.tryParse(age.text);
    final hv = double.tryParse(h.text);
    final wv = double.tryParse(w.text);
    if (a == null || hv == null || wv == null) return;
    final bmr = male ? (10 * wv + 6.25 * hv - 5 * a + 5) : (10 * wv + 6.25 * hv - 5 * a - 161);
    setState(() => result = (bmr * mult).round());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Calories')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(children: [
          TextField(controller: age, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Age', border: OutlineInputBorder())),
          const SizedBox(height: 8),
          TextField(controller: h, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Height (cm)', border: OutlineInputBorder())),
          const SizedBox(height: 8),
          TextField(controller: w, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Weight (kg)', border: OutlineInputBorder())),
          const SizedBox(height: 12),
          Row(children: [
            const Text('Gender: '),
            Radio<bool>(value: true, groupValue: male, onChanged: (v) => setState(() => male = true)),
            const Text('Male'),
            Radio<bool>(value: false, groupValue: male, onChanged: (v) => setState(() => male = false)),
            const Text('Female'),
          ]),
          const SizedBox(height: 8),
          DropdownButton<double>(
            value: mult,
            isExpanded: true,
            items: const [
              DropdownMenuItem(value: 1.2, child: Text('Sedentary')),
              DropdownMenuItem(value: 1.375, child: Text('Lightly active')),
              DropdownMenuItem(value: 1.55, child: Text('Moderately active')),
              DropdownMenuItem(value: 1.725, child: Text('Very active')),
            ],
            onChanged: (v) => setState(() => mult = v!),
          ),
          const SizedBox(height: 16),
          FilledButton(onPressed: _calc, style: FilledButton.styleFrom(minimumSize: const Size(double.infinity, 50)), child: const Text('CALCULATE')),
          const SizedBox(height: 20),
          if (result != null)
            Card(
              color: Colors.orange.withOpacity(0.15),
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Text('$result kcal/day', style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: Colors.orange)),
              ),
            ),
        ]),
      ),
    );
  }
}
