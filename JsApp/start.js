import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import {Text, TouchableWithoutFeedbackComponent, View, Image, TextInput, Button} from 'react-native';
import {gstyles} from '../styles';
import {TouchableWithoutFeedback} from "react-native";



export default function Start() {
    const [text, setValue] = useState('');

    const OnChange = (text)=>{
        setValue(text);
    };

    return (
        <View style={gstyles.container}>
            <Image style={gstyles.logo} source={require('../assets/logo.png')}/>
            <Text style={gstyles.company_name}>TAC-TIC</Text>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Email'/>
            <TextInput secureTextEntry={true} style={gstyles.input} onChangeText={OnChange} placeholder='Password'/>
            <View style={gstyles.button}>
                <Button color = "#F2C8A2" onPress={() => alert("Войти")} title="Войти"/>
            </View>
            <Text style={gstyles.reg} onPress={() => alert("Регистрация")}>Регистрация</Text>
        </View>
    );
}
