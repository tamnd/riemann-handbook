---
id: hol-wc
title: Raising the weight of an ordinary Hilbert eigenform by a congruence
kind: theorem
decl: UpperTheory.Esk.holWC
module: PositivityTheory.AutomorphicForms.PublishedInputs.JacquetLanglands.TorusKernels.MixSeedOf
covers: 1204
status: drafted
drafted_by: writer@claude
---
This theorem makes, from an ordinary cuspidal Hilbert eigenform, a congruent cusp form whose weight is raised at a chosen set of infinite places. It is the one new input of [the mixed-weight seed](/entry/mix-seed-of-alt/), which combines it with an Eisenstein congruence to get ordinary lifts with mixed weights above $\ell$.

## Statement

Let $F$ be a totally real field with $[F:\mathbb{Q}] \geq 2$, $\ell$ an odd prime and $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. Let $|\cdot|_\iota$ be the $\ell$-adic absolute value pulled back to $\mathbb{C}$ by $\iota$. Let $D$ be a datum `LDat`: a bijection $v \mapsto \mathfrak{p}_v$ from the infinite places of $F$ to the places above $\ell$, each of norm $\ell$, with compatible embeddings. So $\ell$ splits completely in $F$. Let $k_0 \geq 4$, and let $\mathfrak{c}$ be a level with finite support, with $\mathfrak{c} = 1$ at each $\mathfrak{p}_v$ and nontrivial at some place of norm 2. Let $\omega$ be a Hecke character of finite order. Let $\varphi$ be a cuspidal automorphic form on $\mathrm{GL}_2$ over $F$, holomorphic of parallel weight $k_0$ and level $K_1(\mathfrak{c})$, with central character $\omega$, and an eigenvector of the normalized Hecke operators $h_{k_0}(w) = Nw^{k_0/2 - 1} U_w$ with eigenvalues $\lambda(w)$ (the predicate `IsEigHol`). Suppose $\varphi$ is ordinary: $|\lambda(\mathfrak{p}_v)|_\iota = 1$ for all $v$.

**Theorem.** For each set $S$ of infinite places and each $B$, there are $t \geq B$ with $(\ell - 1) \mid t$ and a nonzero cusp form $\varphi'$ with these properties. It is holomorphic of weight $k_0 + 2t$ at $v \in S$ and $k_0$ at $v \notin S$, with the same level and central character. It is an eigenvector of the operators $h_{k_0}(w)$ with eigenvalues $\lambda'(w)$. For each finite place $w$,
$$\Bigl|\ell^{\,t \cdot \#\{v \in S : \mathfrak{p}_v = w\}}\, \lambda'(w) - \lambda(w)\Bigr|_\iota < 1.$$

The statement has the shape of a weight congruence in Hida theory. We do not claim that it is a theorem of a given paper.

## Proof

The proof is `holWC_of`, which calls `pf_HolWC`. The steps of `pf_HolWC`:

1. Turn $\varphi$ into a classical form $f_0$ in the finite-dimensional space $M_{k_0}$ of weight $k_0$ (the hypothesis `H1`). Let $N = \dim M_{k_0}$ and $t = (\ell - 1)\,\ell^N \max(B, 1)$.
2. The trace congruence `TrCong`, proved as `pf_TrCong`, compares the traces of products of Hecke operators on $M_{k_0}$ and on the space of weight $k_0 + 2t$ at $S$. After multiplication by normalizing factors (`nz`), both traces are integral and their difference has absolute value at most $\max(|\ell|_\iota^N, |\ell|_\iota^r)$, when each $\mathfrak{p}_v$ occurs at least $r \geq 1$ times in the product. Its proof uses a trace formula `TF` (trace equals a geometric side) and hyperbolic terms, which we have not unfolded.
3. The linear algebra lemma `Fin0` says this. Let two families of commuting operators have congruent traces in this sense. Then a common eigenvector on the first space, with unit eigenvalues at the chosen operators, gives a common eigenvector on the second space with congruent eigenvalues. The choice of $N$ makes $|d|_\iota > |\ell|_\iota^N$ for $1 \leq d \leq \dim M_{k_0}$, which the lemma needs. The lemma plays the role of the lemma of Deligne and Serre (Ann. Sci. ENS 7, 1974, §6), in a form with traces.
4. The other hypotheses (`H2a`, `H2d`, `H2e` and more) turn the new classical eigenform back into the automorphic form $\varphi'$.

## In the Lean code

The theorem is in [MixSeedOf.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/MixSeedOf.lean#L8):

```
holWC_of dAx dTwo' dGood' dReps (pf_GTerm s_GCh s_GUnit s_GMod)
```

The statement `HolWC` is in [IsHolVOf.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/IsHolVOf.lean#L219). The lemmas:

- `holWC_of` in [FinalH.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalH.lean#L47);
- `pf_HolWC` in [PfHolWC.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/PfHolWC.lean#L174);
- `pf_TrCong` in [PfTrCong.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/PfTrCong.lean#L101);
- `Fin0`, proved as `finite_system_holds`, in [ComplexMinusRealLineMeasureCoordinates.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/ComplexMinusRealLineMeasureCoordinates.lean#L189).

The eigenvalues $\lambda'$ are for the operators normalized with $k_0$, not with the new weight. At $w = \mathfrak{p}_v$ with $v \in S$ the two normalizations differ by $Nw^{t} = \ell^t$, the factor in the congruence. The file name `MixSeedOf` does not describe the theorem, and the same file name is used for [the mixed-weight seed](/entry/mix-seed-of-alt/) in another folder.
