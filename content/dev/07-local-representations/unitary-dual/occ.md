---
id: occ
title: Occurrence of a discrete series of U(n) in a discrete series of U(n+1)
kind: theorem
decl: PositivityTheory.RgHe.occ
module: Development.WeilBound.RepresentationTheoryGL.HolomorphicDiscreteSeries.WeightOccurrence.Occ
covers: 396
status: drafted
drafted_by: writer@claude
---
This theorem says that a discrete series $\sigma$ of $U(J_{\varepsilon'})$ occurs in the restriction of a discrete series $\pi$ of $U(J_\varepsilon)$, when the two Harish-Chandra parameters satisfy a word condition. Its one caller is [the real input E](/entry/real-input-e-holds/), which feeds it to `seedB_of` to get the copy of $\sigma$ that the projection $P$ there uses.

## Statement

Take $n \geq 2$, signs $\varepsilon$ on $n+1$ coordinates and $\varepsilon'$ on $n$ coordinates, and a bijection $e$ from $\{1,\dots,n\} \sqcup \{*\}$ to $\{1,\dots,n+1\}$. The embedding $h \mapsto \mathrm{diag}(h, 1)$, moved by $e$, sends $U(J_{\varepsilon'})$ into $U(J_\varepsilon)$. The condition `Gp` asks:

- $\varepsilon$ is `true` at the slot $e(*)$ and restricts to $\varepsilon'$ on the other slots (`Fits`);
- $\varepsilon$ takes the value `false` at least once, and not more often than `true`;
- $\lambda$ and $\mu$ are Harish-Chandra parameters (`IsHCParam`: strictly decreasing, with entries in $\mathbb{Z} + \frac{m-1}{2}$ for a parameter of length $m$);
- two coordinates of opposite sign differ by at least $200(n+1)^3$, in $\lambda$ and in $\mu$ (`GapAtLeast`).

The condition `HeWord` asks: if $x$ and $y$ are neighbours in the merged order of the entries of $\lambda$ and $\mu$, then exactly one of two things holds. Either $x$ and $y$ come from the same parameter, or they carry the same sign.

**Theorem.** Under `Gp` and `HeWord`, for every pair of discrete series $\pi$ with parameter $\lambda$ and $\sigma$ with parameter $\mu$ (`IsDS`), there is a nonzero bounded map $j : \sigma \to \pi$ with $j\,\sigma(h) = \pi(\mathrm{diag}(h,1))\,j$ for all $h \in U(J_{\varepsilon'})$.

`IsDS` asks for an irreducible, unitary, square-integrable representation with a minimal $K$-type at $\lambda + \rho_n - \rho_c$. The name `HeWord` suggests the interlacing condition of H. He, "On the Gan-Gross-Prasad conjecture for U(p,q)", Invent. Math. 209 (2017). We have not checked that the two conditions agree.

## Proof

The proof is `Dec.walk`, which is `occurrence_of_walk`. It takes three facts.

- `Base`: under `Gp` and `HeWord` there is a shift $a \geq 0$, monotone in the merged order, with an occurrence at $(\lambda + a, \mu + a)$. It comes from `RgHe3.base` with `models` and `frame`. That lemma reads off an occurrence far out along a ray in the parameter space.
- `StepL`: an occurrence at $(\lambda, \mu)$ gives one at $(\lambda - e_s, \mu)$, if both satisfy `Gp` and $\lambda_s - \frac12$ is not an entry of $\mu$.
- `StepM`: the same with $\mu_j$ lowered.

The walk inducts on $\sum a$. At each step it lowers the shifted coordinate of least value by 1. The lemma `mono_down` keeps $a$ monotone, `gp_shift` keeps `Gp`, and `cond_down_l` and `cond_down_m` give the side condition. `HeWord` is used only in `Base`.

## In the Lean code

The theorem is in [Occ.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/WeightOccurrence/Occ.lean#L10). `Occ`, `Gp`, `OccAt`, `StepL`, `StepM` and `Base` are in [OccSome.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/WeightOccurrence/OccSome.lean#L49). `HeWord`, `Fits` and `emb` are in [HeBranching.lean](lean:Development/WeilBound/CoreStatements/BranchingTraces/HeBranching.lean#L28). The walk is in [OccurrenceOfWalk.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/FlipDecomposition/OccurrenceOfWalk.lean#L248). We did not open the proofs of `stepL`, `stepM`, `models`, `seed` and `decomposition_existence_holds`.

A second `HeWord` is in `Development/AutomorphicSpectrum/Definitions/MetricPeriods/HeBranching.lean`, in another namespace.
