import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import {Text, TouchableWithoutFeedbackComponent, View} from 'react-native';
import {gstyles} from '../styles';
import {TouchableWithoutFeedback} from "react-native";



export default function Main() {
    const [pos, chPos] = useState(1);
    return (
        <View style={gstyles.container}>
            <View style={gstyles.week}>
                <Text style={[gstyles.selector, {left: (pos*118).toString() + '%'}]}> </Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(1)}>mn</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(2)}>tu</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(3)}>wn</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(4)}>th</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(5)}>fr</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(6)}>sa</Text>
                <Text style={gstyles.title_day} onPress={()=>chPos(7)}>su</Text>
            </View>
            <View style={gstyles.day}>
                <View style={gstyles.important_plan}><Text style={gstyles.plan}>Сходить покушать               9:00-10:00</Text></View>
            </View>
        </View>
    );
}
