---
id: semisimple-potentials-at-newform-eigensystem
title: A Hecke projector on potentials at a newform eigensystem (second name)
kind: theorem
decl: GlobalTheory.T.semisimple_potentials_at_newform_eigensystem
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.SemisimplePotentialsAtNewformEigensystemStatement
covers: 923
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the Hecke projector on potentials](/entry/ss-pot-b-at-newform/), which has the real content. [The Hecke projector for a newform](/entry/hecke-proj-newform/) uses it in its first step, to get the statement $\mathrm{SSPotB}$ at weight $w = k - 2$.

## Statement

Let $g$ be a newform of odd weight $k \ge 3$, level $M$ and character $\chi$. Let $N \ge 5$ with $M \mid N$, and let $\ell$ be a prime with $\ell \nmid N$. Let $\alpha$ be a root of $X^2 - a_\ell(g) X + \chi(\ell)\ell^{k-1}$ with $\alpha^2 \ne \chi(\ell)\ell^{k-1}$ and $\alpha^2 \ne \chi(\ell)\ell^{k-2}$. Let $\lambda$ be a function on the Hecke letters with $\lambda(T_q) = a_q(g)$ for primes $q \nmid N\ell$, $\lambda(U) = \alpha$ and $\lambda(\langle d \rangle) = \chi(d)$ for $d$ prime to $N$.

**Theorem.** $\mathrm{SSPotB}(N, \ell, k-2, \lambda)$ holds: there is a polynomial $P$ in the admitted Hecke letters with $\lambda(P) = 1$ such that $(T - \lambda(T))P$ maps each potential of weight $k - 2$ for $\Gamma_1(N) \cap \Gamma_0(\ell)$ to a trivial potential, for each admitted letter $T$.

The objects are defined in [the entry with the proof](/entry/ss-pot-b-at-newform/).

## Proof

The proof is `exact @GlobalTheory.KZ.SSPotBr.ssPotB_at_newform`. The two statements are the same.

## In the Lean code

The theorem is in [SemisimplePotentialsAtNewformEigensystemStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SemisimplePotentialsAtNewformEigensystemStatement.lean#L10). The file only gives the theorem a name in the namespace `GlobalTheory.T`.
