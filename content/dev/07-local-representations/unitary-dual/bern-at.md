---
id: bern-at
title: Irreducibility of unitary products over one local field
kind: theorem
decl: PositivityTheory.RgUd.All.bernAt
module: Development.WeilBound.RepresentationTheoryGL.UnitaryDualProof.BernsteinExponentBounds.BernAll
covers: 688
status: drafted
drafted_by: writer@claude
---
This theorem proves, for one non-archimedean local field $k$, that the parabolic induction of two irreducible unitary representations of general linear groups is irreducible. Its only caller is [Bernstein's theorem](/entry/bernstein-unitary-product-irreducible/), which quantifies over $k$. The proof joins three facts about Bernstein-Zelevinsky derivatives; two of them come from the statement on mirabolic-invariant forms in [ThmB](/entry/thm-b/).

## Statement

Let $k$ be a non-archimedean local field. With the notation of [Bernstein's theorem](/entry/bernstein-unitary-product-irreducible/):

**Theorem** ($\mathrm{BernAt}(k)$). If $\pi_1$ of $\mathrm{GL}_r(k)$ and $\pi_2$ of $\mathrm{GL}_t(k)$ are smooth, irreducible and unitarizable, then $\pi_1 \times \pi_2$ is irreducible.

## Proof

Fix a nontrivial character $\psi$ of $k$ and let $\pi^{(h)}$ be the $h$-th derivative of $\pi$, as in [the Leibniz rule](/entry/leibniz-ord/). The proof is `Prod.Final.bern_of` applied to three statements:

- `DerivTop`, from `Form.U.Final.derivTop` and [ThmB](/entry/thm-b/): if $\pi$ is smooth, irreducible and unitarizable and $\pi^{(h)}$, $h \ge 1$, is its highest nonzero derivative, then $\pi^{(h)} \otimes |\det|^{(1-h)/2}$ is irreducible and unitarizable.
- `DerivPos`, from `Form.U.Final.derivPos` and ThmB: for the same $\pi$ and $1 \le i$ below the highest derivative, the central character $\omega$ of each nonzero subquotient of $\pi^{(i)} \otimes |\det|^{(1-i)/2}$ has $|\omega(z)| < 1$ for $|z| < 1$.
- `LeibnizOrd`, from [`leibnizOrd`](/entry/leibniz-ord/): the derivatives of $\pi_1 \times \pi_2$ have a filtration with layers $\pi_1^{(i)} \times \pi_2^{(\ell - i)}$, up to twists. This is the Leibniz rule of I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. ENS 10 (1977).

From these, `bern_of` builds two statements about $X = \pi_1 \times \pi_2$. `TopProdD` says that the highest nonzero derivative $X^{(h)}$, $h > 0$, is a twist of a product of two irreducible unitarizable representations. `PosProdD` bounds the central eigenvalues on the lower derivatives $X^{(j)}$, $j < h$. Then `bern_of_parts` uses `prod_irreducible`, a strong induction on $r + t$. By induction, $X^{(h)}$ is irreducible. $X$ is unitarizable and admissible, so each subrepresentation has a complement. `nd_of_irr` shows that each nonzero subrepresentation has a nonzero $h$-th derivative. `irreducible_of_top` concludes that $X$ is irreducible, because a splitting $X = S \oplus T$ would split $X^{(h)}$.

## In the Lean code

The theorem is at [BernAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/BernAll.lean#L23). `BernAt`, `DerivTop` and `DerivPos` are in [IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L74). `bern_of` is in [BernOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/BernOf.lean#L14) and `bern_of_parts` in [NormEqOneOfUnitarisable.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/CentralProducts/UnitarisableHypotheses/NormEqOneOfUnitarisable.lean#L295). The file [ThmBChar0.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/ThmBChar0.lean#L13) has a copy, `bern`, for characteristic zero only, with the same three inputs. Because `bern` also calls `bern_of`, `derivTop`, `derivPos` and `leibnizOrd`, these are not counted below `bernAt`; most of the 688 declarations below it are in [the case of characteristic $p$](/entry/tp-final-thm-t/).
