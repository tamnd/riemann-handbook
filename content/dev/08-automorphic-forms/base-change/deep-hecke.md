---
id: deep-hecke
title: Base change matching for spherical functions with a deep factor
kind: theorem
decl: UpperTheory.ConvolutionTheory.H.deepHecke
module: Development.AutomorphicArithmetic.Foundations.Convolution.SphericalHeckeOperators.DeepHecke
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves the base change matching of orbital integrals for spherical Hecke functions on $\mathrm{GL}_n$ over an unramified extension of local fields, but only for functions whose Satake transform has a chosen factor $g$. Its only user is [local Hecke matching at inert places](/entry/loc-hecke-inert/), which applies it to completions of a number field. The work is in `deepAbs` and `thMatch`; this theorem checks that orbital integrals meet the conditions of `deepAbs`.

## Statement

Let $E/k$ be a finite Galois extension of nonarchimedean local fields, with $k$ of characteristic 0. Suppose that a uniformizer of $k$ is a uniformizer of $E$, so $E/k$ is unramified, and that $\sigma$ generates $\mathrm{Gal}(E/k)$. Let $l = [E:k]$. Normalize the Haar measures $\mu_E$, $\mu_k$ on $\mathrm{GL}_n(E)$, $\mathrm{GL}_n(k)$ so that $\mathrm{GL}_n(\mathcal{O}_E)$ and $\mathrm{GL}_n(\mathcal{O}_k)$ have volume 1. Let $\mathcal{S}$ be the Satake transform from the spherical Hecke algebra into $\mathbb{C}[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$, and let $b_l$ be the algebra map $x^a \mapsto x^{la}$. Call $\phi$ on $\mathrm{GL}_n(E)$ and $f$ on $\mathrm{GL}_n(k)$ *matching* if:

1. for $\delta$ with $N\delta$ regular semisimple and $N\delta = h\gamma h^{-1}$, the twisted orbital integral of $\phi$ at $\delta$ equals the orbital integral of $f$ at $\gamma$, when the measures on the centralizers correspond under conjugation by $h$;
2. the orbital integral of $f$ is 0 at each regular semisimple $\gamma$ that is not a norm.

**Theorem.** Let $P$ be a finite set of symmetric Laurent polynomials and $z \in (\mathbb{C}^\times)^n$. Then there is a symmetric polynomial $g$ (no negative exponents) with $g(z) \neq 0$, such that for each $p$ in the span of $P$: if $\mathcal{S}(h) = gp$ and $\mathcal{S}(f) = b_l(gp)$, then $h$ and $f$ match.

The full base change fundamental lemma for the spherical Hecke algebra (Clozel, "The fundamental lemma for stable base change", Duke Math. J. 61, 1990) has no factor $g$. The Lean statement is weaker.

## Proof

`unrQ` gives $q_E = q_k^l$. `deepAbs` then gives $g$ and this property: let $\Lambda_E$, $\Lambda_k$ be linear on locally constant functions of compact support, zero on the commutators $a * b - b * a$ with $a$ the unit or the indicator of an Iwahori double coset, and with $\Lambda_E(\theta_E(a)) = \Lambda_k(\theta_k(la))$ for each strictly decreasing $a \in \mathbb{Z}^n$. Here $\theta(a)$ is the normalized indicator of $I\varpi^a I$. Then $\Lambda_E(h) = \Lambda_k(f)$. We have not unfolded the proof of `deepAbs`.

For clause 1, take $\Lambda_E$ the twisted orbital integral at $\delta$ and $\Lambda_k$ the orbital integral at $\gamma$. Then $\gamma$ is regular semisimple, because $N\delta$ is conjugate to $\gamma$ and so has the same (separable) characteristic polynomial. Linearity comes from `twOrbLin_holds` and `orbLin_holds`. The commutators vanish by `twOrbComm_holds` and `orbComm_holds`; the twisted case needs $a$ to be $\sigma$-invariant, which is `sigInv`. The identity on $\theta(a)$ is clause 1 of `thMatch`. For clause 2, take $\Lambda_E = 0$; clause 2 of `thMatch` gives the identity on $\theta(a)$.

## In the Lean code

The theorem is in [DeepHecke.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/DeepHecke.lean#L81). Matching is `Loc.Match` in [Match.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/TwistedLocalOrbits/Match.lean#L13). The lemmas it calls:

- `deepAbs`, `thMatch`, `sigInv`, `unrQ`, `defBridge` in the same folder;
- `twOrbLin_holds`, `orbLin_holds`, `twOrbComm_holds`, `orbComm_holds` in `QuotFubiniHolds.lean`;
- private lemmas `lin_of`, `comm_zero`, `reg_of_norm` in this file.

The name "deep" probably refers to the lemma `depth` in [MemSuppMono.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SphericalHeckeOperators/MemSuppMono.lean#L69), which `deepAbs` calls. It gives an $m$ such that, for each $a$ with $a_i - a_j \geq m$ when $i < j$, each product $x^a \Delta p$ with $p \in P$ has strictly decreasing exponents ($\Delta$ is a fixed product of factors $x_i - s x_j$, $s$ a constant). We have not checked how `deepAbs` builds $g$ from this.
