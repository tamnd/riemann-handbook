---
id: chapter-m-holds
title: An ordinary eigenfunctional and an Eisenstein measure for an ordinary newform
kind: theorem
decl: GlobalTheory.EisM.chapterM_holds
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinaryEisensteinEigenfunctionalExists
covers: 548
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{CuspidalUnitaryTwistsClaim}$. [The ordinary Eisenstein eigenfunctional theorem](/entry/ordinary-eisenstein-eigenfunctional-exists/) is the same statement under a second name. The proof is a pass-through: it chooses a level and calls [the result at a fixed level](/entry/chapter-m-of-level/), which has the real content and the definitions in full.

## Statement

Let $\ell$ be an odd prime, $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, and $e \ge 1$. Let $g$ be a newform of weight $k = 2e+1$, level $M$ with $\ell \nmid M$ and character $\chi_g$, with $|\iota^{-1} a_\ell(g)| = 1$. Let $\psi$ be a [[Dirichlet character|JR4QSEFXWF]] modulo $\ell$ and $N_0 \ge 1$ with $\ell \nmid N_0$.

**Theorem.** There are $N$, characters $\chi, \theta$ modulo $N$, numbers $\alpha, v$, a functional $\lambda$ on $q$-expansions and integers $c_1, d_1$ such that:

1. $N \ge 5$, $M \mid N$, $N_0 \mid N$, $\ell \nmid N$, and $\chi$ agrees with $\chi_g$ on integers prime to $N$;
2. $\alpha$ is an $\iota$-unit root of $X^2 - a_\ell(g) X + \chi(\ell)\ell^{2e}$;
3. $\lambda$ is a Hecke eigenfunctional for $g$ on forms of level $N\ell$ and character $\chi$, with $U_\ell$ eigenvalue $\alpha$, and it kills the other characters;
4. $\chi(-1) = -1$ and $\theta(-1) = (-1)^e\psi(-1)$;
5. $\lambda$ and a product of two Eisenstein series built from $\theta$ give an $\ell$-adic measure whose value at $x \mapsto \psi(x)x^{-e}$ is $v \ne 0$;
6. $c_1, d_1 > 1$ are smoothing integers prime to $6N\ell$.

## Proof

1. Take a prime $r \ge \ell + 7$.
2. `depleted_newform_prim` removes from $g$ the coefficients $a_n$ with $n$ not prime to $MN_0r$. The result is an eigenform of level $N = M(MN_0r)^2$.
3. $N$ is divisible by $M$, $N_0$ and the prime $r \ge 7$, and not by $\ell$. So [`chapterM_of_level`](/entry/chapter-m-of-level/) applies and gives the rest.

## In the Lean code

The theorem is in [OrdinaryEisensteinEigenfunctionalExists.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinaryEisensteinEigenfunctionalExists.lean#L109), and the statement in [CuspidalUnitaryTwistsClaim.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/CuspidalUnitaryTwistsClaim.lean#L13). It calls `depleted_newform_prim` in [DepletedNewformPrim.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/DepletedNewformPrim.lean#L15), `chapterM_of_level` in the same file, and `Nat.exists_infinite_primes`.

The hypothesis `hl2` ($\ell \ne 2$) is introduced but never used. The statement name says "cuspidal unitary twists", but the statement is about an eigenfunctional and a measure.
