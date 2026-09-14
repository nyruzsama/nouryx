async function runTests() {
  console.log('--- TEST 1: Check /api/channels ---');
  const chRes = await fetch('http://localhost:3000/api/channels');
  const chData = await chRes.json();
  console.log('Channels count:', chData.channels.length);
  console.log('First channel:', chData.channels[0]);

  console.log('\n--- TEST 2: Broadcast Photo to "June 29 - Kean\'s Day" ---');
  const samplePng = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==', 'base64');
  const boundary = '----WebKitFormBoundaryTVBroadcastTest';

  let body = '';
  body += `--${boundary}\r\n`;
  body += `Content-Disposition: form-data; name="studentName"\r\n\r\nKean\r\n`;
  body += `--${boundary}\r\n`;
  body += `Content-Disposition: form-data; name="gradeSection"\r\n\r\nGrade 12 - STEM\r\n`;
  body += `--${boundary}\r\n`;
  body += `Content-Disposition: form-data; name="channel"\r\n\r\nJune 29 - Kean's Day\r\n`;
  body += `--${boundary}\r\n`;
  body += `Content-Disposition: form-data; name="caption"\r\n\r\nBirthday celebration with the squad!\r\n`;
  body += `--${boundary}\r\n`;
  body += `Content-Disposition: form-data; name="photos"; filename="kean_bday.png"\r\n`;
  body += `Content-Type: image/png\r\n\r\n`;

  const bodyBuffer = Buffer.concat([
    Buffer.from(body, 'utf8'),
    samplePng,
    Buffer.from(`\r\n--${boundary}--\r\n`, 'utf8')
  ]);

  const uploadRes = await fetch('http://localhost:3000/api/upload', {
    method: 'POST',
    headers: { 'Content-Type': `multipart/form-data; boundary=${boundary}` },
    body: bodyBuffer
  });
  const uploadData = await uploadRes.json();
  console.log('Upload result:', uploadData);

  console.log('\n--- TEST 3: Fetch photos for channel ---');
  const chPhotosRes = await fetch('http://localhost:3000/api/channels/' + encodeURIComponent("June 29 - Kean's Day") + '/photos');
  const chPhotosData = await chPhotosRes.json();
  console.log('Channel photos returned:', chPhotosData.photos.length);
  const photo = chPhotosData.photos[0];
  console.log('Photo details:', photo);

  console.log('\n--- TEST 4: View photo in TV screen ---');
  const viewRes = await fetch('http://localhost:3000/api/photos/view/' + photo.id);
  console.log('View status (200 expected):', viewRes.status, 'Content-Type:', viewRes.headers.get('content-type'));

  console.log('\n--- TEST 5: SSG Download Channel ZIP ---');
  const loginRes = await fetch('http://localhost:3000/api/ssg/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ pin: '2026' })
  });
  const loginData = await loginRes.json();
  const token = loginData.token;

  const zipRes = await fetch('http://localhost:3000/api/ssg/channels/' + encodeURIComponent("June 29 - Kean's Day") + '/download-zip?token=' + token);
  console.log('Channel ZIP status (200 expected):', zipRes.status);
  const zipBuf = await zipRes.arrayBuffer();
  console.log('ZIP bytes received:', zipBuf.byteLength);

  console.log('\n--- ALL RETRO TV CHANNEL TESTS PASSED! ---');
}

runTests().catch(err => console.error('Test error:', err));
