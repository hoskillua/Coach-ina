import 'dart:io';

import 'package:get/get.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

class GameController extends GetxController {
  PickedFile? _imageFile;
  XFile? pickedFile;
  XFile? pickedFile2;
  RxBool isLoading = true.obs;
  final ImagePicker _picker = ImagePicker();

  RxString responseString = "".obs;

  Future loadImage(filepath, url, game) async {
    if (game == "king") {
      var request = http.MultipartRequest('POST', Uri.parse(url));
      request.fields['selected_game'] = game;
      request.files.add(http.MultipartFile(
          'hand_image',
          pickedFile!.readAsBytes().asStream(),
          File(pickedFile!.path).lengthSync(),
          filename: filepath.split("/").last));
      var response = await request.send();
      responseString = (await response.stream.bytesToString()).obs;
      return response.stream.bytesToString();
    } else {
      var request = http.MultipartRequest('POST', Uri.parse(url));
      request.fields['selected_game'] = game;
      request.files.add(http.MultipartFile(
          'hand_image',
          pickedFile!.readAsBytes().asStream(),
          File(pickedFile!.path).lengthSync(),
          filename: filepath.split("/").last));

      request.files.add(http.MultipartFile(
          'ground_image',
          pickedFile2!.readAsBytes().asStream(),
          File(pickedFile!.path).lengthSync(),
          filename: filepath.split("/").last));

      var response = await request.send();
      responseString = (await response.stream.bytesToString()).obs;
      return response.stream.bytesToString();
    }
  }

  Future uploadImage(String game) async {
    try {
      isLoading(true);
      await _pickImage();
      if (game != "game") await _pickImage2();
      await loadImage(_imageFile, "http://34.125.150.242/api/predict", game);
    } finally {
      isLoading(false);
    }
  }

  Future _pickImage() async {
    try {
      pickedFile = await _picker.pickImage(source: ImageSource.camera);
    } catch (e) {
      print("Image picker error " + e.toString());
    }
  }

  Future _pickImage2() async {
    try {
      pickedFile2 = await _picker.pickImage(source: ImageSource.camera);
    } catch (e) {
      print("Image picker error " + e.toString());
    }
  }
}
