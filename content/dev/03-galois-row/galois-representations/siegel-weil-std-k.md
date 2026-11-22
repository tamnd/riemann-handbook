---
id: siegel-weil-std-k
title: The Siegel-Weil formula for the theta lift of the Galois row
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilFinFinal
covers: 1680
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem proves a Siegel-Weil formula on doubled unitary groups: a theta integral over a definite unitary group is a special value of a Siegel Eisenstein series. Its user is [the tools of the theta lift](/entry/tools-holds-k/), which makes from it the field `swFull` of the tool kit of the Galois row. The theorem is a copy of [the Siegel-Weil formula](/entry/siegel-weil-std/) with one hypothesis changed. Below it are 1,680 declarations.

## Statement

Let $E/F$ be a CM extension with conjugation $\sigma$, and $B$ a base datum with an additive character $\psi$ of $\mathbb{A}_F/F$. Suppose (`GoodK`) that $E$ contains an $x$ with $x^2 = -d$ for an integer $d > 0$, that $E/F$ is unramified, that $\psi$ is standard, and that $\psi$ is unramified at a given finite set of places and at the inert places, which do not lie over 2 and have norm greater than 3.

Let $A$ be a space of size $m \geq 1$ and $Y$ a space of size $n \geq 1$ over $E$. One of them is hermitian and the other is skew-hermitian, and $A$ is definite. Let $\chi$ be a Hecke character of $\mathbb{A}_E^\times$ whose restriction to $\mathbb{A}_F^\times$ is 1 on $F^\times N(\mathbb{A}_E^\times)$ and $(-1)^m$ elsewhere. Let $\omega$ be a Weil representation of the doubled group $G_2 = U(Y \oplus -Y)$ on Schwartz functions, with an action $S$ of $U_A(\mathbb{A})$ and a functional $l$ (the doubling datum). Let $K$ be the standard maximal compact subgroup of $G_2(\mathbb{A})$, and $a$ the height with $a(pk) = |\det t|$ for $p$ in the Siegel parabolic with Levi part $t$. Let $\mu$ be a Haar measure on $U_A(\mathbb{A})$ and $D$ a fundamental domain for $U_A(F)$. Let $\Phi$ be a $K$-finite Schwartz function and $s_0 = \tfrac{m-n}{2}$.

**Theorem.** For each $x \in G_2(\mathbb{A})$, the Siegel Eisenstein series of the section $g \mapsto a(g)^{s-s_0}\, l(\omega(g)\Phi)$ converges for $\operatorname{Re} s$ large, has a meromorphic continuation to $\mathbb{C}$ that is analytic at $s_0$, and

$$E(x, s_0, \Phi) = c \cdot \frac{1}{\mu(D)} \int_D \theta\bigl(\omega(x) S_g \Phi\bigr)\, d\mu(g), \qquad c = \begin{cases} 1 & n < m, \\ 2 & n \geq m. \end{cases}$$

Here $\theta(\Phi)$ is the sum of $\Phi$ over the rational points. This has the shape of the Siegel-Weil formula of Weil (Acta Math. 113, 1965). We have not compared its constants with a published form.

## Proof

`Act.ctSplit_of_k` proves the constant term split `CTSplit_k`, and [`siegelWeilStd_of_ct_k`](/entry/siegel-weil-std-of-ct-k/) gives the formula from it. All the work is below these two. The [Siegel-Weil chapter](/proof/siegel-weil/) follows the same proof for the copy without `_k`.

## In the Lean code

The theorem is in [SiegelWeilFinFinal.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinFinal.lean#L15). Its proof is

```
siegelWeilStd_of_ct_k (Act.ctSplit_of_k kfour.auxiliaryExistence_holds kfour.coefEx_k)
```

The statement `SiegelWeilStd_k` is in [BaseKnownTheoremsS.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/BaseKnownTheoremsS.lean#L13). Its text is the text of `SiegelWeilStd` in [HypothesesS.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/HypothesesS.lean#L11), except for the first hypothesis: `UpperTheory.TP.W.GoodK σ B` in place of `B.IsGood σ`. The two structures ([SplitStab.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/HalfIndexLattices/SplitStab.lean#L18), [WeilTensorModels.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean#L350)) differ in one field: `GoodK` asks for a square root of $-d$ in $E$, `IsGood` asks that $E/\mathbb{Q}$ is Galois. Neither condition implies the other in general, so the code proves the formula again, with its own copies of the definitions.

Odd points:

- `ctSplit_of_k` ([SiegelWeilActTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActTop.lean#L17)) has the form `fun _ _ => …`. It does not use its two arguments, `auxiliaryExistence_holds` and `coefEx_k`. The copy `Act.ctSplit_of` without `_k` does the same.
- The field of `GoodK` that asks for the square root of $-d$ has the name `galois`.
- `auxiliaryExistence_holds` proves `SiegelWeilDatumProperties`: a Haar measure of covolume 1, a rational Weyl element, and topological facts on $G_2(\mathbb{A})$. Its name does not say this.
