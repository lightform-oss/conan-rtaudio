#include <iostream>
#include "RtAudio.h"

int main()
{
    RtAudio audio;

    // Determine the number of devices available
    auto device_count = audio.getDeviceCount();
    std::cout << "Found " << device_count << " devices\n\n";

    // Scan through devices for various capabilities
    for (auto i = 0; i < device_count; ++i) {
        auto info = audio.getDeviceInfo(i);
        if (info.probed == true) {
            std::cout << "device " << i << ":\n";
            std::cout << "\tis default output: " << info.isDefaultOutput << "\n";
            std::cout << "\tis default input: " << info.isDefaultInput << "\n";
            std::cout << "\tname: " << info.name << "\n";
            std::cout << "\toutput channels: " << info.outputChannels << "\n";
            std::cout << "\tinput channels: " << info.inputChannels << "\n";
            std::cout << "\tpreferred sample rate: " << info.preferredSampleRate << "\n";
            std::cout << "\n";
        }
    }
    return 0;
}
