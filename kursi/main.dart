import 'package:flutter/material.dart';


import 'insert.dart';
//import 'package:pucon/home.dart';

void main() => runApp( MyApp());

class MyApp extends StatelessWidget {
   MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return  MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ListView(
        children: [
          InsertData(),
        ],
      ),
    );
  }
}
