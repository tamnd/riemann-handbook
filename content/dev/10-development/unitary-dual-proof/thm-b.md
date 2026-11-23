---
id: thm-b
title: Mirabolic-invariant forms on an irreducible unitary representation are multiples of the invariant form
kind: theorem
decl: PositivityTheory.RgUd.All.thmB
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.BernsteinExponentBounds.BernAll
covers: 687
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ThmB}(k)$ for each non-archimedean local field $k$: on a smooth irreducible unitarizable representation of $\mathrm{GL}_{n+1}(k)$, a sesquilinear form that is invariant under the mirabolic subgroup is a multiple of the invariant form. The proof is one line that joins three lemmas: $\mathrm{ThmT} \Rightarrow \mathrm{ThmA} \Rightarrow \mathrm{ThmB}$. Its only caller is [`bernAt`](/entry/bern-at/), which uses it twice, for `DerivTop` and `DerivPos`.

## Statement

Let $P_{n+1} \subseteq \mathrm{GL}_{n+1}(k)$ be the mirabolic subgroup: the $g$ whose last row is $(0, \dots, 0, 1)$. A *distribution* on $\mathrm{GL}_{n+1}(k)$ is a $\mathbb{C}$-linear form on functions, and only its values on locally constant functions with compact support enter.

$\mathrm{ThmA}(k)$: if a distribution $\Lambda$ on $\mathrm{GL}_{n+1}(k)$ is invariant under conjugation by $P_{n+1}$, then it is invariant under conjugation by $\mathrm{GL}_{n+1}(k)$.

**Theorem** ($\mathrm{ThmB}(k)$). Let $\pi$ on $V$ be a smooth irreducible representation of $\mathrm{GL}_{n+1}(k)$ and $B$ a positive definite invariant Hermitian form on $V$. Let $\beta$ be a sesquilinear form on $V$ with $\beta(\pi(p)v, \pi(p)w) = \beta(v, w)$ for $p \in P_{n+1}$. Then $\beta = cB$ for some $c \in \mathbb{C}$.

$\mathrm{ThmA}$ has the form of Bernstein's theorem on $P$-invariant distributions (J. N. Bernstein, Lecture Notes in Math. 1041, 1984). We have not compared $\mathrm{ThmB}$ with that paper.

## Proof

The proof is `AB.Final.thmB k (AB.Final.thmA k (thmT k))`.

1. [`thmT`](/entry/all-thm-t/) gives $\mathrm{ThmT}(k)$.
2. `AB.Final.thmA` gives $\mathrm{ThmA}$ from $\mathrm{ThmT}$ by `thmA_of_core`. The input `CoreX` says: given $\mathrm{ThmT}$, a distribution on $M_{n+1}(k)$ invariant under conjugation by $P_{n+1}$ is invariant under $\mathrm{GL}_{n+1}(k)$. `thmA_of_core` moves a test function on $\mathrm{GL}_{n+1}(k)$ to $M_{n+1}(k)$ by a map `extZ`, which we have not unfolded.
3. `AB.Final.thmB` gives $\mathrm{ThmB}$ from $\mathrm{ThmA}$. Irreducible smooth representations are admissible. `formTraceDistrGL` gives a distribution attached to $B$. Then `kirillovForm_of_theoremA'`, with a Schur lemma for invariant forms (`formSchurGL`), gives the scalar.

We have not unfolded the proof of `CoreX` or of `formTraceDistrGL`.

## In the Lean code

The theorem is at [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L21). `ThmA` and `ThmB` are in [IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L64). The two steps are in [ThmA.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/ThmA.lean#L13). `thmA_of_core` is in [MemSBIffSupportedIn.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/MemSBIffSupportedIn.lean#L65), and `thmB_of_kirillov` in [FormTraceDistrGL.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/TraceDistributionsGL/FormTraceDistrGL.lean#L110). The file ThmBChar0.lean has `thmB_char0`, the same term with the characteristic-zero [`T.Final.thmT`](/entry/t-final-thm-t/).
