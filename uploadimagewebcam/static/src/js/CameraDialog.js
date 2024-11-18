/** @odoo-module */

import { Dialog } from "@web/core/dialog/dialog";
import { useRef, onMounted, useState, Component, onWillUnmount } from "@odoo/owl";

export class CameraDialog extends Component {
    setup() {
        super.setup();
        this.video = useRef('video');
        this.image = useRef('image');
        this.state = useState({
            img: false,
            cameras: [], // List of available cameras
            selectedCameraId: null, // The ID of the selected camera
        });

        onMounted(async () => {
            await this.getCameras(); // Get available cameras on component mount
            await this.startCamera(this.state.selectedCameraId); // Start the camera feed with the selected device
        });

        onWillUnmount(() => {
            this.stopCamera();
        });
    }

    /**
     * Retrieves the list of available cameras (video input devices).
     */
    async getCameras() {
        const devices = await navigator.mediaDevices.enumerateDevices();//call enumerateDevices(); method
        
        const videoDevices = devices.filter(device => device.kind === 'videoinput');
        this.state.cameras = videoDevices;
        this.state.selectedCameraId = videoDevices.length > 0 ? videoDevices[0].deviceId : null;
        
    }

    /**
     * Starts the camera with the specified device ID.
     */
    async startCamera(deviceId) {
        
        if (this.video.el) {
            const stream = await navigator.mediaDevices.getUserMedia({
                video: { deviceId: { exact: deviceId } },
                audio: false
            });
            this.video.el.srcObject = stream;
        }
    }

    /**
     * Stops the current camera feed.
     */
    stopCamera() {
        if (this.video.el && this.video.el.srcObject) {
            this.video.el.srcObject.getVideoTracks().forEach((track) => {
                track.stop();
            });
        }
    }

    /**
     * Handles the camera change event when the user selects a different camera.
     */
    async onCameraChange(event) {
        const newCameraId = event.target.value;
        this.state.selectedCameraId = newCameraId;
        this.stopCamera();
        await this.startCamera(newCameraId);
    }

    _cancel() {
        (this.env.dialogData).close();
        this.stopCamera();
    }

    _confirm() {
        let video = this.video.el;
        let image = this.image.el;
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const canvasContext = canvas.getContext("2d");
        canvasContext.drawImage(video, 0, 0);
        this.state.img = canvas.toDataURL('image/jpeg');
        this.img_binary = this.state.img.split(',')[1];
        video.classList.add('d-none');
        image.classList.remove('d-none');
        image.src = this.state.img;
    }

    async _save() {
        await this.props.parent.props.record.update({ [this.props.parent.props.name]: this.img_binary });
        this.state.img = "data:image/jpeg;base64," + this.img_binary;
        (this.env.dialogData).close();
        this.stopCamera();
    }

    _reset() {
        this.img_binary = false;
        this.state.img = false;
        this.video.el.classList.remove('d-none');
        this.image.el.classList.add('d-none');
    }
}

CameraDialog.template = "capture_image_field.camera_dialog";
CameraDialog.components = { Dialog };
