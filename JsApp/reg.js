import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import {Text, TouchableWithoutFeedbackComponent, View, Image, TextInput, Button} from 'react-native';
import {gstyles} from '../styles';
import {TouchableWithoutFeedback} from "react-native";



export default function Reg() {
    const [text, setValue] = useState('');

    const OnChange = (text)=>{
        setValue(text);
    };

    return (
        <View style={gstyles.container}>
            <Image style={gstyles.logo} source={require('../assets/logo.png')}/>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Email'/>
            <TextInput style={gstyles.input} onChangeText={OnChange} placeholder='Name'/>
            <TextInput secureTextEntry={true} style={gstyles.input} onChangeText={OnChange} placeholder='Password'/>
            <TextInput secureTextEntry={true} style={gstyles.input} onChangeText={OnChange} placeholder='Confirm Password'/>
            <View style={gstyles.button}>
                <Button color = "#F2C8A2" onPress={() => alert("Зарегистрироваться")} title="Зарегистрироваться"/>
            </View>
        </View>
    );
}
