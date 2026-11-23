---
id: rest-prime-bound-full
title: The bound on the rest terms at one prime
kind: theorem
decl: GroundTheory.Heights₂.Heights.RestTerms.RestPrimeBound.full
module: GroundTheory.HeightsAndTheta.Heights.RemainderTerms.Imports
covers: 616
status: drafted
drafted_by: writer@claude
---
This theorem bounds the contribution $M(p)$ of one prime $p > B_0$ to the rest terms by $1.5\, f X (fra+1)|D_c| \log p / p^2$. Its one user is [`RestBound.full`](/entry/rest-bound-full/), which sums this bound over the primes. The proof joins two bounds on single rest terms, which come from the characters of the symmetric group, with two elementary series bounds.

## Statement

Let $f, r, a \ge 1$ and $N = r + a$. Let $R = \mathbb{Q}[x_{\tau,i}]$, with $\tau < f$ and $i < N$, and let $V = \prod_\tau \prod_{i<j} (x_{\tau,i} - x_{\tau,j})$. The flag integral of $\Phi \in R$ is
$$\textstyle\int \Phi = \sum_\alpha [x^\alpha]\Phi \cdot [x^\alpha]V \cdot \alpha!,$$
that is, $(V(\partial)\Phi)(0)$. A small block $c$ splits each row $\tau$ into $r$ roots $y_{\tau,i}$ and $a$ roots $z_{\tau,i}$. For $c$ = last, $y_{\tau,i} = x_{\tau,a+i}$ and $z_{\tau,i} = x_{\tau,i}$. For $c$ = first, $y_{\tau,i} = -x_{\tau,i}$ and $z_{\tau,i} = x_{\tau,r+i}$. Put $\mu = \sum_{\tau,i} y_{\tau,i}$, $\Delta_c = \prod_\tau V(y_\tau) V(z_\tau)$, $F_c = \mu^{fra+1}\Delta_c$, $D_c = \int \mu^{fra}\Delta_c$ and $X = 2(ra + r + a)$.

A power sum decomposition of $F_c$ is a family $Q_{k,\tau} \in R$ with $F_c = \sum_{k=1}^{N} \sum_\tau p_k(x_\tau) Q_{k,\tau}$, where $p_k(x_\tau) = \sum_i x_{\tau,i}^k$. The rest term of $G$ is $T(k,\tau,G) = k \int G\, Q_{k,\tau}$. For a prime $p$, maps $s(p,n,\tau) < f$ and signs $e(p,n,\tau,k) = \pm 1$, let
$$M(p) = \log p \sum_\tau \sum_{k=2}^{N} \sum_{n \ge 0} p^{-(n+1)k}\, e(p,n+1,\tau,k)\, T\bigl(k,\tau,p_{k-1}(y_{s(p,n+1,\tau)})\bigr).$$

**Theorem.** If $4fN^2 \le B_0$, then $F_c$ has a power sum decomposition, and for every one, all $s$ and $e$, and every prime $p > B_0$,
$$|M(p)| \le 1.5\, f X \frac{\log p}{p^2}\,(fra+1)\,|D_c|.$$

## Proof

Let $C = (fra+1)|D_c|$.

1. **One term.** For $2 \le k \le N$ and all $\tau, \tau'$, $|T(k,\tau,p_{k-1}(y_{\tau'}))| \le C X^{k-1}/k!$. For $\tau' = \tau$ this is `SameFactorBound.full`; for $\tau' \ne \tau$ it is `OtherFactorBound.full`. The first also gives the decomposition. By Imports.lean, both rest on `SameFactorFormula`, which writes the term through Schur polynomials with coefficients $\chi^{a+\nu}((k-1),1^{ra+1})$, on `CharacterBound` ($|\chi^\lambda(\rho)|$ is at most the number of standard tableaux of shape $\lambda$, a case of $|\chi(g)| \le \chi(1)$, Isaacs, Character Theory of Finite Groups, Lemma 2.15) and on `HookSumBound`. We have not followed those proofs.
2. **The sum over $n$.** Since $p > 4fN^2$ and $X \le \tfrac32 N^2$, we get $X \le 3p/8$ (`XOverPrime`). A geometric series gives $|\sum_n p^{-(n+1)k} c_n| \le 2p^{-k} \sup|c_n|$ (`RestInnerTsumBound`).
3. **The sum over $k$.** $\sum_{k=2}^{N} 2p^{-k} X^{k-1}/k! \le 1.5\, X/p^2$ (`RestKSumBound`).
4. The sum over $\tau$ gives the factor $f$.

Steps 2 to 4 are `RestPrimeBoundOfFactor.full`.

## In the Lean code

The theorem is in [Imports.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Imports.lean#L566), with statement at [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Statements.lean#L319). The assembly `RestPrimeBound.proof` is in [PRestPrimeBound.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PRestPrimeBound.lean#L10). It drops the facts $D_c \ne 0$ and, for $\tau' \ne \tau$, $T = 0$ when $ra < k - 1$; this bound does not need them. The flag integral is defined as the pairing with $V$ above, not as an integral over a flag variety.
