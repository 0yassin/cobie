import { MeshGradient } from '@paper-design/shaders-react'
import './App.css'

function App() {
  return (
    <main className='relative min-h-screen w-screen overflow-hidden text-white font-sans'>
      <div className='absolute inset-0 w-full h-full z-0'>
        <MeshGradient
          style={{ width: '100%', height: '100%' }}
          colors={["#121212", "#241d9a", "#121212"]}
          distortion={0.8}
          swirl={0.03}
          grainMixer={0.44}
          grainOverlay={0.11}
          speed={0.56}
        />
      </div>

      <div className='relative z-10 flex flex-col min-h-screen w-screen items-center text-center'>
        <nav className='w-full z-20 h-fit border-b content-center items-center border-[#F8F7F5]/40 flex justify-between pl-8 bg-[#E5E4E2]/10'>
          <span className="text-[26px] font-medium">Cobie</span>
          <div className='flex gap-0 h-full'>
            <button className='px-8 h-full hover:bg-[#F8F7F5]/20 py-4 transition-colors '>
              <span className='text-[#E5E4E2]'>Download</span>
            </button>
            <button className='px-8 h-full hover:bg-[#F8F7F5]/20 py-4 transition-colors '>
              <span className='text-[#E5E4E2]'>Source</span>
            </button>
          </div>
        </nav>
        <div className='w-screen h-screen -mt-20 flex justify-center items-center'>
          <h1 className='text-[64px] font-medium text-[#F8F7F5]'>
            Build with Cobie
          </h1>
        </div>
        
      <div className='w-full flex justify-center mb-12 -mt-36'>
        <div className='w-[75%] aspect-video bg-[#1F1F25]/70 border border-[#F8F7F5]/40 rounded-2xl '></div>
      </div>
  

      </div>
    </main>
  )
}

export default App