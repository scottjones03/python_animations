import numpy as np
from OpenGL import GL
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QApplication


class OpenGLWidget(QOpenGLWidget):

    def initializeGL(self):
        vertices = np.array([0.0, 1.0, -1.0, -1.0, 1.0, -1.0], dtype=np.float32)

        bufferId = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, bufferId)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_STATIC_DRAW)

        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 2, GL.GL_FLOAT, GL.GL_FALSE, 0, None)

    def wireCube(self, cubeEdges, cubeVertices):
        GL.glBegin(GL.GL_LINES)
        for cubeEdge in cubeEdges:
            for cubeVertex in cubeEdge:
                GL.glVertex3fv(cubeVertices[cubeVertex])
        GL.glEnd()

    def paintGL(self):
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)


app = QApplication([])
widget = OpenGLWidget()
widget.show()
app.exec_()