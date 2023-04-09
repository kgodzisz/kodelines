# kodelines
<p>I wrote a script that outputs the number of lines of code from specified file extensions. In reality, the script can also be used to output lines of text, where we define the file format. However, its primary use is to output lines of code. Just like in the previous two cases, I create a Docker image that I use. However, if you want, I can also share the script itself. So you can run it using Python installed on your local system. The script is available in the Github repository.</p><br />

<p><strong>To download files from Github:</strong></p>
<p><code>git clone https://github.com/kgodzisz/kodelines.git</code></p><br />

<p><strong>Create your own image in your local repository:</strong></p>
<p><code>docker build -t kodelines .</code></p><br />

<p><strong>Run the tool:</strong></p>
<p><code>docker run --rm -v /path/to/folder:/app kodelines</code></p><br />

<p><strong>The second way is to download the prepared file from the Docker Hub repository:</strong></p>
<p><code>docker run --rm -v /path/to/folder:/app kgodzisz/kodelines</code></p><br />

<p><strong>Description of the options used in the commands:</strong> </p>
<p><code>--rm </code>- the container will be automatically removed after it is exited; </p>
<p><code>-v </code>- the path to the folder where the files for which you want to display the number of lines of code are located; </p>
<p><code>kodelines </code>- the name of the created image that we want to use; </p>
<p><code>kgodzisz/kodelines </code>- the address of the image on the DockerHub platform.</p><br />

<p><strong>Blog</strong>: https://dockeryzacjaswiata.pl</p>
<p><strong>Docker Hub</strong>: https://hub.docker.com/r/kgodzisz/kodelines</p>
